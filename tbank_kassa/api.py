from typing import Unpack

from .client import TBankKassaClient
from .enums import TBankKassaEnvironment
from .logger import logger
from .models import dicts, request, response


class TBankAPI:
    def __init__(
        self,
        terminal_key: str,
        password: str,
        environment: TBankKassaEnvironment = TBankKassaEnvironment.PROD,
    ):
        self._client = TBankKassaClient(
            environment=environment,
        )
        self._terminal_key = terminal_key
        self._password = password
        logger.info(
            'T-Bank API is ready now!'
                '\n\tTerminal "%s".'
                '\n\tEnvironment "%s".',
            self._terminal_key,
            environment.value,
        )

    async def ainit_payment(self, **kwargs: Unpack[dicts.InitDict]):
        return await self._client.apost(
            request.Init(
                password=self._password,
                terminal_key=self._terminal_key,
                **kwargs,
            ),
            response.Payment,
        )

    def init_payment(self, **kwargs: Unpack[dicts.InitDict]):
        return self._client.post(
            request.Init(
                password=self._password,
                terminal_key=self._terminal_key,
                **kwargs,
            ),
            response.Payment,
        )
