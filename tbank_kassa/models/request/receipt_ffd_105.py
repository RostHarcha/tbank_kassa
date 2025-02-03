from typing import Literal

from pydantic import (
    BaseModel,
    EmailStr,
    Field,
    ValidationError,
    model_validator,
)

from . import enums
from .item import Item


class ReceiptFFD105(BaseModel):
    items: list[Item] = Field(
        serialization_alias='Items',
    )
    """
    Массив позиций чека с информацией о товарах.
    """

    ffd_version: Literal['1.05'] = Field(
        serialization_alias='FfdVersion',
        default='1.05',
        frozen=True,
    )
    """
    Версия ФФД.
    """

    email: EmailStr | None = Field(
        serialization_alias='Email',
        max_length=64,
        default=None,
    )
    """
    Электронная почта клиента. Параметр должен быть заполнен, если не
    передано значение в параметре `phone`.
    """

    phone: str | None = Field(
        serialization_alias='Phone',
        max_length=64,
        default=None,
    )
    """
    Телефон клиента в формате `+{Ц}`. Параметр должен быть заполнен, если
    не передано значение в параметре `email`.
    """
    taxation: enums.Taxation = Field(
        serialization_alias='Taxation',
    )
    """
    Система налогообложения.
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
