import tbank_kassa

TBANK_KASSA_TERMINAL_KEY='1733316170548DEMO'
TBANK_KASSA_PASSWORD='12$##&HSG6mrxV4H'
TBANK_KASSA_TEST=False
TBANK_KASSA_WEBHOOK_URL='https://chatlabs.su/collector-bot/backend/api/transactions/webhook/'



tbank = tbank_kassa.TBankAPI(
    terminal_key=TBANK_KASSA_TERMINAL_KEY,
    password=TBANK_KASSA_PASSWORD,
    environment=(
        tbank_kassa.enums.TBankKassaEnvironment.TEST
        if TBANK_KASSA_TEST
        else tbank_kassa.enums.TBankKassaEnvironment.PROD
    ),
)

payment = tbank.init_payment(
    amount=120,
    order_id='test-order-with-recipe11',
    description='descr',
    customer_key='518485500',
    notification_url=TBANK_KASSA_WEBHOOK_URL,
    receipt=tbank_kassa.models.ReceiptFFD105(
        items=[
            tbank_kassa.models.Item(
                name='Полная оплата',
                price=120,
                quantity=1,
                amount=120,
                tax=tbank_kassa.models.Tax.NONE,
            )
        ],
        email='rostiki.com@mail.ru',
        taxation=tbank_kassa.models.Taxation.USN_INCOME_OUTCOME,
    )
)

print(payment)
