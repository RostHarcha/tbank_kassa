from datetime import datetime

from pydantic import Field, HttpUrl

from .. import fields
from . import enums
from .receipt_ffd_12 import ReceiptFFD12
from .receipt_ffd_105 import ReceiptFFD105
from .request import TokenRequest
from .shop import Shop


class Init(TokenRequest):
    """
    Метод инициирует платежную сессию.
    """
    _method = 'Init'

    terminal_key: fields.TerminalKey = Field(
        serialization_alias='TerminalKey',
    )
    """
    Идентификатор терминала.

    Выдается мерчанту Т‑Кассой при заведении терминала.
    """

    amount: fields.Amount = Field(
        serialization_alias='Amount',
    )
    """
    Сумма платежа.
    """

    order_id: str = Field(
        serialization_alias='OrderId',
        max_length=36,
    )
    """
    Идентификатор заказа в системе мерчанта.
    Должен быть уникальным для каждой операции.
    """

    description: str | None = Field(
        serialization_alias='Description',
        max_length=140,
        default=None,
    )
    """
    Описание заказа. Значение параметра будет отображено на платежной форме.

    Для привязки и одновременной оплаты по СБП поле обязательное.
    При оплате через СБП эта информация отобразится в мобильном банке клиента.
    """

    customer_key: str | None = Field(
        serialization_alias='CustomerKey',
        max_length=36,
        default=None,
    )
    """
    Идентификатор клиента в системе мерчанта.

    - Обязателен, если передан атрибут Recurrent.
    - Если был передан в запросе, в нотификации будет указан CustomerKey и
        его CardId.
    - Нужен для сохранения карт на платежной форме — платежи в один клик.
    - Необязателен при рекуррентных платежах через СБП.
    """

    recurrent: str | None = Field(
        serialization_alias='Recurrent',
        max_length=1,
        default=None,
    )
    """
    Признак родительского рекуррентного платежа.
    Обязателен для регистрации автоплатежа.

    Если передается и установлен в `Y`, регистрирует платеж как рекуррентный.
        В этом случае после оплаты в нотификации на `AUTHORIZED` будет
        передан параметр `RebillId` для использования в методе `Charge`.
        Для привязки и одновременной оплаты по CБП передавайте `Y`.

    Значение зависит от атрибутов:

    - `OperationInitiatorType` — в методе `/init`,
    - `Recurrent` — в методе `/Init`.
    """

    payment_type: enums.PaymentType | None = Field(
        default=None,
        serialization_alias='PayType',
    )
    """
    Определяет тип проведения платежа — двухстадийная или одностадийная оплата:

    - `PaymentType.ONE_STAGE` — одностадийная оплата,
    - `PaymentType.TWO_STAGE` — двухстадийная оплата.

    Если параметр:
    - передан — используется его значение
    - не передан — значение из настроек терминала.
    """

    language: enums.Language | None = Field(
        serialization_alias='Language',
        default=None,
    )
    """
    Язык платежной формы:

    - Language.RUS — русский,
    - Language.ENG — английский.

    Если не передан, форма откроется на русском языке.
    """

    notification_url: HttpUrl | None = Field(
        serialization_alias='NotificationURL',
        default=None,
    )
    """
    URL на веб-сайте мерчанта, куда будет отправлен POST-запрос о статусе
    выполнения вызываемых методов — настраивается в личном кабинете.

    Если параметр:
    - передан — используется его значение,
    - не передан — значение из настроек терминала.
    """

    success_url: HttpUrl | None = Field(
        serialization_alias='SuccessURL',
        default=None,
    )
    """
    URL на веб-сайте мерчанта, куда будет переведен клиент в случае успешной
    оплаты — настраивается в личном кабинете.

    Если параметр:
    - передан — используется его значение,
    - не передан — значение из настроек терминала.
    """

    fail_url: HttpUrl | None = Field(
        serialization_alias='FailURL',
        default=None,
    )
    """
    URL на веб-сайте мерчанта, куда будет переведен клиент в случае неуспешной
    оплаты — настраивается в личном кабинете.

    Если параметр:
    - передан — используется его значение,
    - не передан — значение из настроек терминала.
    """

    time_to_live: datetime | None = Field(
        serialization_alias='RedirectDueDate',
        default=None,
    )
    """
    Cрок жизни ссылки или динамического QR-кода СБП, если выбран этот
    способ оплаты.

    Если текущая дата превышает дату, которая передана в этом параметре,
    ссылка для оплаты или возможность платежа по QR-коду становятся
    недоступными и платёж выполнить нельзя.

    Максимальное значение — 90 дней от текущей даты.
    Минимальное значение — 1 минута от текущей даты.

    Если не передан, принимает значение 24 часа для платежа и 30 дней
    для счета.

    Выставление счета через личный кабинет

    Если параметр RedirectDueDate не был передан, проверяется настроечный
    параметр платежного терминала REDIRECT_TIMEOUT, который может содержать
    значение срока жизни ссылки в часах.

    Если его значение:
    - больше нуля — оно будет установлено в качестве срока жизни ссылки или
    динамического QR-кода;
    - меньше нуля — устанавливается значение по умолчанию: 1440 мин. (1 сутки).
    """

    extra: dict | None = Field(
        serialization_alias='DATA',
        default=None,
    )
    """
    Позволяет передавать дополнительные параметры по операции и задавать
    определенные настройки в формате `ключ:значение`.

    Максимальная длина для каждого передаваемого параметра:
    - ключ — 20 знаков;
    - значение — 100 знаков.

    Максимальное количество пар ключ:значение — 20.

    Для `МСС 4814` обязательно передать значение в параметре Phone.

    Требования по заполнению:
    - минимум — 7 символов,
    - максимум — 20 символов,
    - разрешены только цифры, исключение — первый символ может быть +.

    Для `МСС 6051` и `6050` обязательно передавать параметр `account` — номер
    электронного кошелька, не должен превышать 30 символов.
    """

    receipt: ReceiptFFD105 | ReceiptFFD12 | None = Field(
        serialization_alias='Receipt',
        default=None,
    )
    """
    Данные чека. Обязателен, если подключена онлайн-касса.
    """

    shops: list[Shop] | None = Field(
        serialization_alias='Shops',
        default=None,
    )
    """
    Данные маркетплейса. Обязателен для маркетплейсов.
    """

    descriptor: str | None = Field(
        serialization_alias='Descriptor',
        default=None,
    )
    """
    Динамический дескриптор точки.
    """