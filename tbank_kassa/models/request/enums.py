from enum import StrEnum


class PaymentType(StrEnum):
    ONE_STAGE = 'O'
    TWO_STAGE = 'T'


class Language(StrEnum):
    RUS = 'ru'
    ENG = 'en'


class Taxation(StrEnum):
    """
    Система налогообложения.
    """

    OSN = 'osn'
    "общая СН"

    USN_INCOME = 'usn_income'
    "упрощенная СН (доходы)"

    USN_INCOME_OUTCOME = 'usn_income_outcome'
    "упрощенная СН (доходы минус расходы)"

    ENVD = 'envd'
    "единый налог на вмененный доход"

    ESN = 'esn'
    "единый сельскохозяйственный налог"

    PATENT = 'patent'
    "патентная СН"


class Tax(StrEnum):
    """
    Ставка НДС
    """

    NONE = 'none'
    "без НДС"

    VAT0 = 'vat0'
    "НДС по ставке 0%"

    VAT5 = 'vat5'
    "НДС по ставке 5%"

    VAT7 = 'vat7'
    "НДС по ставке 7%"

    VAT10 = 'vat10'
    "НДС по ставке 10%"

    VAT20 = 'vat20'
    "НДС по ставке 20%"

    VAT105 = 'vat105'
    "НДС чека по расчетной ставке 5/105"

    VAT107 = 'vat107'
    "НДС чека по расчетной ставке 7/107"

    VAT110 = 'vat110'
    "НДС чека по расчетной ставке 10/110"

    VAT120 = 'vat120'
    "НДС чека по расчетной ставке 20/120"
