from decimal import Decimal

from pydantic import (
    BaseModel,
    Field,
    ValidationError,
    model_validator,
)

from .. import fields
from . import enums


class ItemFFD105(BaseModel):
    name: str = Field(
        serialization_alias='Name',
        max_length=128,
    )
    """
    Наименование товара.
    """

    price: fields.Amount = Field(
        serialization_alias='Price',
    )
    """
    Цена.
    """

    quantity: Decimal = Field(
        serialization_alias='Quantity',
        max_digits=8,
        decimal_places=3,
    )
    """
    Количество или вес товара. Максимальное количество символов — 8, где
    целая часть — не больше 5 знаков, дробная — не больше 3 знаков для АТОЛ,
    и 2 знаков для CloudPayments.
    """

    amount: fields.Amount = Field(
        serialization_alias='Amount',
    )
    """
    Стоимость товара. Произведение `quantity` и `price`.
    """

    tax: enums.Tax = Field(
        serialization_alias='Tax',
    )
    """
    Ставка НДС.
    """

    @model_validator(mode='after')
    def validate_amount(self):
        if self.amount != self.price * self.quantity:
            msg = '`amount` must be equal to `quantity * price`'
            raise ValidationError(msg)
        return self
