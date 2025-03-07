import hashlib
from datetime import datetime
from decimal import Decimal
from typing import Annotated, ClassVar, Literal, Optional, Union

from pydantic import (
    ConfigDict,
    EmailStr,
    Field,
    HttpUrl,
    computed_field,
    model_validator,
)

from .. import enums, validators
from . import fields
from .base import BaseSchema


class BaseData(BaseSchema):
    model_config = ConfigDict(extra='forbid')


class Common(BaseData):
    additionalProperties: Optional[str] = None
    OperationInitiatorType: Optional[enums.OperationInitiatorType] = None


class LongPay(BaseData):
    pass


class TPay(BaseData):
    Device: Optional[enums.Device] = None
    DeviceOs: Optional[str] = None
    DeviceWebView: Optional[bool] = None
    DeviceBrowser: Optional[str] = None
    TinkoffPayWeb: Optional[bool] = None


class AgentData(BaseSchema):
    AgentSign: Optional[enums.AgentSign] = None
    OperationName: Optional[str] = Field(default=None, max_length=64)
    Phones: Optional[list[fields.PhoneNumberField]] = None
    ReceiverPhones: Optional[list[fields.PhoneNumberField]] = None
    TransferPhones: Optional[list[fields.PhoneNumberField]] = None
    OperatorName: Optional[str] = Field(default=None, max_length=64)
    OperatorAddress: Optional[str] = Field(default=None, max_length=243)
    OperatorInn: Optional[fields.InnField] = None


class SupplierInfo(BaseSchema):
    Phones: Optional[list[fields.PhoneNumberField]] = None
    Name: Optional[str] = Field(default=None, max_length=239)
    Inn: Optional[fields.InnField] = None


class BaseItem(BaseSchema):
    AgentData: Optional['AgentData'] = None
    SupplierInfo: Optional['SupplierInfo'] = None
    Name: str = Field(max_length=128)
    Price: int
    Quantity: fields.Quantity
    Tax: enums.Tax

    @computed_field
    @property
    def Amount(self) -> int:
        return int(self.Quantity * self.Price)


class Item_FFD_105(BaseItem):
    PaymentMethod: Optional[enums.PaymentMethod] = None
    PaymentObject: Optional[enums.PaymentObject_FFD_105] = None
    Ean13: Optional[fields.Ean13] = None
    ShopCode: Optional[str] = None


class MarkCode(BaseSchema):
    MarkCodeType: enums.MarkCodeType
    Value: str


class MarkQuantity(BaseSchema):
    Numerator: Optional[int]
    Denominator: Optional[int]


class SectoralItemProps(BaseSchema):
    FederalId: str
    Date: fields.DateField
    Number: str
    Value: str


class Item_FFD_12(BaseItem):
    PaymentMethod: enums.PaymentMethod
    PaymentObject: enums.PaymentObject_FFD_12
    UserData: Optional[str] = None
    Excise: Optional[Decimal] = Field(
        default=None, max_digits=10, decimal_places=2, gt=Decimal('0')
    )
    CountryCode: Optional[fields.CountryCode] = None
    DeclarationNumber: Optional[str] = Field(default=None, max_length=32)
    MeasurementUnit: fields.MeasurementUnit
    MarkProcessingMode: Optional[Literal['0']] = None
    MarkCode: Optional['MarkCode'] = None
    MarkQuantity: Optional['MarkQuantity'] = None
    SectoralItemProps: Optional['SectoralItemProps'] = None


class Payments(BaseSchema):
    Cash: Optional[int] = Field(default=None, lt=10**14)
    Electronic: int = Field(lt=10**14)
    AdvancePayment: Optional[int] = Field(default=None, lt=10**14)
    Credit: Optional[int] = Field(default=None, lt=10**14)
    Provision: Optional[int] = Field(default=None, lt=10**14)


class ClientInfo(BaseSchema):
    Birthdate: Optional[fields.DateField] = None
    Citizenship: Optional[str] = None
    DocumentСode: Optional[enums.DocumentСode] = None
    DocumentData: Optional[str] = None
    Address: Optional[str] = Field(default=None, max_length=256)


class BaseReceipt(BaseSchema):
    _ffd_version: ClassVar[str]
    Taxation: enums.Taxation
    Email: Optional[EmailStr] = Field(default=None, max_length=64)
    Phone: Optional[fields.PhoneNumberField] = None
    Payments: Optional['Payments'] = None
    Items: list[BaseItem]

    @computed_field
    @property
    def FfdVersion(self) -> str:
        return self._ffd_version

    @property
    def Amount(self) -> int:
        return sum(item.Amount for item in self.Items)


class Receipt_FFD_105(BaseReceipt):
    _ffd_version = '1.05'
    Items: list[Item_FFD_105]


class Receipt_FFD_12(BaseReceipt):
    _ffd_version = '1.2'
    ClientInfo: Optional['ClientInfo'] = None
    Customer: Optional[str] = None
    CustomerInn: Optional[fields.InnField] = None
    Items: list[Item_FFD_12]


class Shop(BaseSchema):
    ShopCode: str
    Amount: int
    Name: Optional[str] = Field(default=None, max_length=128)
    Fee: Optional[str] = None


class Init(BaseSchema):
    Password: str = Field(max_length=20, exclude=True)
    TerminalKey: str = Field(max_length=20)
    Amount: Optional[int] = Field(default=None, lt=10**10)
    OrderId: str = Field(max_length=36)
    Description: Optional[str] = Field(default=None, max_length=140)
    CustomerKey: Optional[str] = Field(default=None, max_length=36)
    Recurrent: Optional[Literal['Y']] = None
    PayType: Optional[enums.PayType] = None
    Language: Optional[enums.Language] = None
    NotificationURL: Optional[HttpUrl] = None
    SuccessURL: Optional[HttpUrl] = None
    FailURL: Optional[HttpUrl] = None
    RedirectDueDate: Optional[datetime] = None
    DATA: Optional[
        Annotated[
            Union[dict, TPay, Common, LongPay], validators.validate_length(20)
        ]
    ] = Field(default=None)
    Receipt: Optional[Union[Receipt_FFD_105, Receipt_FFD_12]] = None
    Shops: Optional[list[Shop]] = None
    Descriptor: Optional[str] = None

    @computed_field
    @property
    def Token(self) -> str:
        token_dict = {
            k: str(v).lower() if isinstance(v, bool) else v
            for k, v in {
                **self.model_dump(
                    mode='json', exclude={'Token'}, exclude_unset=True
                ),
                'Password': self.Password,
            }.items()
            if isinstance(v, (str, int, float, bool))
        }
        token = ''.join(str(token_dict[key]) for key in sorted(token_dict))
        return hashlib.sha256(token.encode('utf-8')).hexdigest()

    @model_validator(mode='after')
    def check_amount(self):
        if self.Amount is None and self.Receipt is None:
            msg = 'One of `Amount` or `Receipt` is required.'
            raise ValueError(msg)
        if self.Receipt:
            if not self.Receipt.Items and self.Amount is None:
                msg = '`Receipt.Items` can not be empty if `Amount` is not specified.'
                raise ValueError(msg)
            if self.Receipt.Items:
                self.Amount = self.Receipt.Amount
            if self.Amount is not None and self.Amount != self.Receipt.Amount:
                msg = '`self.Amount` must be equal to `self.Receipt.Amount`.'
                raise ValueError(msg)
        return self
