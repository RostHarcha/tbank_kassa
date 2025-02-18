from typing import Literal

from pydantic import (
    BaseModel,
    EmailStr,
    Field,
    ValidationError,
    model_validator,
)

from . import enums
from .client_info import ClientInfo
from .item_ffd_12 import ItemFFD12


class ReceiptFFD12(BaseModel):
    ffd_version: Literal['1.2'] = Field(
        serialization_alias='FfdVersion',
        default='1.2',
        frozen=True,
        init=False,
    )
    """Версия ФФД."""

    client_info: ClientInfo | None = Field(
        serialization_alias='ClientInfo',
        default=None,
    )
    """Информация по клиенту."""

    taxation: enums.Taxation = Field(
        serialization_alias='Taxation',
    )
    """
    `Тег ФФД: 1055`

    Система налогообложения.
    """

    email: EmailStr | None = Field(
        serialization_alias='Email',
        max_length=64,
        default=None,
    )
    """
    `Тег ФФД: 1008`

    Электронная почта клиента. Параметр должен быть заполнен, если не
    передано значение в параметре `phone`.
    """

    phone: str | None = Field(
        serialization_alias='Phone',
        max_length=64,
        default=None,
    )
    """
    `Тег ФФД: 1008`

    Телефон клиента в формате `+{Ц}`. Параметр должен быть заполнен, если
    не передано значение в параметре `email`.
    """

    customer: str | None = Field(
        serialization_alias='Customer',
        default=None,
    )
    """
    `Тег ФФД: 1227`

    Идентификатор/имя клиента.
    """

    customer_inn: str | None = Field(
        serialization_alias='CustomerInn',
        default=None,
    )
    """
    `Тег ФФД: 1228`

    ИНН клиента.
    """
    items: list[ItemFFD12] = Field(
        serialization_alias='Items',
    )
    """
    Массив позиций чека с информацией о товарах.

    Атрибуты, предусмотренные в протоколе для отправки чеков по маркируемым
    товарам, не являются обязательными для товаров без маркировки. Если
    используется ФФД 1.2, но реализуемый товар не подлежит маркировке, поля
    можно не отправлять или отправить со значением `None`.
    """

    @model_validator(mode='after')
    def validate_email_or_phone(self):
        if not any([self.email, self.phone]):
            msg = (
                'At least one of the fields from `email` and `phone` '
                'is required.'
            )
            raise ValidationError(msg)
        return self
