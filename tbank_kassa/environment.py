from pydantic import BaseModel, HttpUrl


class TBankAPIEnvironment(BaseModel):
    name: str
    base_url: HttpUrl


TEST = TBankAPIEnvironment(
    name='TEST',
    base_url=HttpUrl('https://rest-api-test.tinkoff.ru/v2'),
)

PROD = TBankAPIEnvironment(
    name='PROD',
    base_url=HttpUrl('https://securepay.tinkoff.ru/v2'),
)
