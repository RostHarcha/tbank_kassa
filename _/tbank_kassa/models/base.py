import hashlib
from typing import Any, override

from pydantic import BaseModel, ConfigDict, Field


class TBankObject(BaseModel):
    """Базовая модель Т-Банка"""  # noqa: RUF002

    model_config = ConfigDict(
        use_enum_values=True,
        validate_assignment=True,
        frozen=True,
        populate_by_name=True,
    )

    @override
    def model_dump(self, **kwargs) -> dict[str, Any]:
        kwargs.setdefault('mode', 'json')
        kwargs.setdefault('by_alias', True)
        kwargs.setdefault('exclude_unset', True)
        return super().model_dump(**kwargs)


class MutableTBankObject(TBankObject):
    """Базовая изменяемая модель Т-Банка"""  # noqa: RUF002

    model_config = ConfigDict(
        frozen=False,
    )


class Request(TBankObject):
    """Запрос к API Т-Банка"""  # noqa: RUF002


class TokenRequest(Request):
    """Запрос к API Т-Банка, подписанный токеном"""  # noqa: RUF002

    password: str = Field(
        max_length=20,
        alias='Password',
    )
    """
    Используется для подписи запросов/ответов. Является секретной информацией,
    известной только мерчанту и Т‑Кассе.

    Пароль находится в личном кабинете мерчанта.
    """

    token: str = Field(
        alias='Token',
        init=False,
    )
    """Токен запроса."""

    def sign(self, password: str) -> None:
        token_dict = {}
        data = self.model_dump(exclude={'token'})
        for key, value in {**data, 'Password': password}.items():
            if isinstance(value, dict):
                continue
            if isinstance(value, bool):
                value = str(value).lower()
            token_dict[key] = str(value)
        token = ''.join(token_dict[key] for key in sorted(token_dict))
        self.token = hashlib.sha256(token.encode('utf-8')).hexdigest()


class Response(TBankObject):
    """Ответ API Т-Банка"""  # noqa: RUF002

    success: bool = Field(
        validation_alias='Success',
    )
    """
    Успешность прохождения запроса.
    """

    error_code: str = Field(
        validation_alias='ErrorCode',
        max_length=20,
    )
    """
    Код ошибки. 0 в случае успеха.
    """

    error_message: str | None = Field(
        validation_alias='Message',
        max_length=255,
        default=None,
    )
    """
    Краткое описание ошибки.
    """

    error_details: str | None = Field(
        validation_alias='Details',
        default=None,
    )
    """
    Подробное описание ошибки.
    """
