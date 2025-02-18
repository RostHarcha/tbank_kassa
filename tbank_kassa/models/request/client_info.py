from datetime import date

from pydantic import BaseModel, ConfigDict, Field

from . import enums


def date_to_str(date_: date) -> str:
    return date_.strftime('%d.%m.%Y')


class ClientInfo(BaseModel):
    model_config = ConfigDict(
        json_encoders={
            date: date_to_str,
        },
        coerce_numbers_to_str=True,
    )

    birthdate: date | None = Field(
        serialization_alias='Birthdate',
        default=None,
    )
    """
    `Тег ФФД: 1243`

    Дата рождения клиента.
    """

    citizenship: int | None = Field(
        serialization_alias='Citizenship',
        default=None,
    )
    """
    `Тег ФФД: 1244`

    Числовой код страны, гражданином которой является клиент. Код страны
    указывается в соответствии с Общероссийским классификатором стран мира ОКСМ.
    """

    document_code: enums.DocumentCode | None = Field(
        serialization_alias='DocumentСode',
        default=None,
    )
    """
    `Тег ФФД: 1245`

    Числовой код вида документа, удостоверяющего личность.
    """

    document_data: str | None = Field(
        serialization_alias='DocumentData',
        default=None,
    )
    """
    Тег ФФД: 1246

    Реквизиты документа, удостоверяющего личность — например, серия и номер
    паспорта.
    """

    address: str | None = Field(
        serialization_alias='Address',
        max_length=256,
        default=None,
    )
    """
    `Тег ФФД: 1254`

    Адрес клиента-грузополучателя.
    """
