from decimal import Decimal

from pydantic import (
    BaseModel,
    Field,
    ValidationError,
    model_validator,
)

from .. import fields
from . import enums


class ItemFFD12(BaseModel):
    name: str = Field(
        serialization_alias='Name',
        max_length=128,
    )
    """
    `Тег ФФД: 1030`

    Наименование товара.
    """

    price: fields.Amount = Field(
        serialization_alias='Price',
    )
    """
    `Тег ФФД: 1079`

    Цена.
    """

    quantity: Decimal = Field(
        serialization_alias='Quantity',
        max_digits=8,
        decimal_places=3,
    )
    """
    `Тег ФФД: 1023`

    Количество или вес товара. Максимальное количество символов — 8, где
    целая часть — не больше 5 знаков, дробная — не больше 3 знаков для АТОЛ,
    и 2 знаков для CloudPayments.
    """

    amount: fields.Amount = Field(
        serialization_alias='Amount',
    )
    """
    `Тег ФФД: 1043`

    Стоимость товара. Произведение `quantity` и `price`.
    """

    tax: enums.Tax = Field(
        serialization_alias='Tax',
    )
    """
    Ставка НДС.
    """

    payment_object: enums.PaymentObject = Field(
        serialization_alias='PaymentObject',
    )
    """
    `Тег ФФД: 1212`

    Значения реквизита «признак предмета расчета» — тег 1212, таблица 101.
    """

    measurement_unit: enums.MeasurementUnit = Field(
        serialization_alias='MeasurementUnit',
    )

    """
    `Тег ФФД: 2108`

    Единицы измерения. Передавать в соответствии с ОК 015-94 (МК 002-97).

    Возможна передача произвольных значений.

    Обязателен, если версия ФД онлайн-кассы — 1.2.
    """

    @model_validator(mode='after')
    def validate_amount(self):
        if self.amount != self.price * self.quantity:
            msg = '`amount` must be equal to `quantity * price`'
            raise ValidationError(msg)
        return self
