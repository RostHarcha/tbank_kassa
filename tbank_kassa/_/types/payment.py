from decimal import Decimal

from pydantic import Field, HttpUrl

from .response import Response


class Payment(Response):
    """
    Платеж
    """

    terminal_key: str = Field(
        alias='TerminalKey',
        max_length=20,
    )
    """
    Идентификатор терминала.

    Выдается мерчанту Т‑Кассой при заведении терминала.
    """

    amount: Decimal = Field(
        alias='Amount',
        max_digits=10,
        decimal_places=2,
    )
    """
    Сумма платежа.
    """

    order_id: str = Field(
        alias='OrderId',
        max_length=36,
    )
    """
    Идентификатор заказа в системе мерчанта.
    """

    status: str = Field(
        alias='Status',
        max_length=20,
    )
    """
    Статус транзакции.
    """

    payment_id: str = Field(
        alias='PaymentId',
        max_length=20,
    )
    """
    Идентификатор платежа в системе Т‑Кассы.
    """

    payment_url: HttpUrl | None = Field(
        alias='PaymentURL',
        default=None,
    )
    """
    Ссылка на платежную форму.
    Параметр возвращается только для мерчантов без PCI DSS.
    """
