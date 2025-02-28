from enum import StrEnum


class Status(StrEnum):
    """Статус платежа"""

    NEW = 'NEW'
    """Платеж создан."""

    AUTHORIZED = 'AUTHORIZED'
    """
    Деньги захолдированы на карте клиента. Ожидается подтверждение операции.
    """

    CONFIRMED = 'CONFIRMED'
    """Операция подтверждена."""

    PARTIAL_REVERSED = 'PARTIAL_REVERSED'
    """Частичная отмена."""

    REVERSED = 'REVERSED'
    """Операция отменена, когда произошло холдирование."""

    CANCELED = 'CANCELED'
    """Операция отменена, когда создана платежная ссылка."""

    PARTIAL_REFUNDED = 'PARTIAL_REFUNDED'
    """Произведён частичный возврат."""

    REFUNDED = 'REFUNDED'
    """Произведён возврат."""

    REJECTED = 'REJECTED'
    """Списание денежных средств закончилась ошибкой."""

    DEADLINE_EXPIRED = 'DEADLINE_EXPIRED'
    """
    Автоматическое закрытие сессии, которая превысила срок пребывания в статусе
    3DS_CHECKING — больше 36 часов.
    """
