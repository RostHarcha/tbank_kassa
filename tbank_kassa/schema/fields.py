from datetime import date, datetime
from decimal import Decimal
from typing import Annotated, Union

from phonenumbers import PhoneNumberFormat
from pydantic import AfterValidator, Field, StringConstraints
from pydantic_extra_types.phone_numbers import PhoneNumber, PhoneNumberValidator

from .. import enums

PhoneNumberField = Annotated[
    Union[str, PhoneNumber],
    PhoneNumberValidator(
        number_format=PhoneNumberFormat.to_string(PhoneNumberFormat.E164),
    ),
]

AtolQuantity = Annotated[Decimal, Field(max_digits=8, decimal_places=3)]

CloudPaymentsQuantity = Annotated[
    Decimal, Field(max_digits=8, decimal_places=2)
]

Quantity = Union[AtolQuantity, CloudPaymentsQuantity]

AtolEan13 = Annotated[
    str,
    StringConstraints(
        pattern=r'(^[a-fA-F0-9]{2}$)|(^([a-fA-F0-9]{2}\s){1,31}[a-fA-F0-9]{2}$)',
        max_length=95,
    ),
]

CloudKassirEan13 = Annotated[
    str,
    StringConstraints(
        pattern=r'^[A-Fa-f0-9]{16,300}$',
        min_length=16,
        max_length=300,
    ),
]

OrangeDataEan13 = Annotated[
    str,
    StringConstraints(
        min_length=12,
        max_length=44,
    ),
]

Ean13 = Union[AtolEan13, CloudKassirEan13, OrangeDataEan13]

InnField = Annotated[
    str,
    StringConstraints(
        pattern=r'^\d{10}(\d{2})?$',
        min_length=10,
        max_length=12,
    ),
]

DateField = Annotated[
    date,
    AfterValidator(lambda value: datetime.strptime(value, '%d.%m.%Y').date()),
]

CountryCode = Annotated[
    str, StringConstraints(pattern=r'^\d{3}$', min_length=3, max_length=3)
]

MeasurementUnit = Annotated[
    Union[str, enums.MeasurementUnit],
    StringConstraints(min_length=1, max_length=10),
]
