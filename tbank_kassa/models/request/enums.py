from enum import Enum, StrEnum


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
    'общая СН'

    USN_INCOME = 'usn_income'
    'упрощенная СН (доходы)'

    USN_INCOME_OUTCOME = 'usn_income_outcome'
    'упрощенная СН (доходы минус расходы)'

    ENVD = 'envd'
    'единый налог на вмененный доход'

    ESN = 'esn'
    'единый сельскохозяйственный налог'

    PATENT = 'patent'
    'патентная СН'


class Tax(StrEnum):
    """
    Ставка НДС
    """

    NONE = 'none'
    'без НДС'

    VAT0 = 'vat0'
    'НДС по ставке 0%'

    VAT5 = 'vat5'
    'НДС по ставке 5%'

    VAT7 = 'vat7'
    'НДС по ставке 7%'

    VAT10 = 'vat10'
    'НДС по ставке 10%'

    VAT20 = 'vat20'
    'НДС по ставке 20%'

    VAT105 = 'vat105'
    'НДС чека по расчетной ставке 5/105'

    VAT107 = 'vat107'
    'НДС чека по расчетной ставке 7/107'

    VAT110 = 'vat110'
    'НДС чека по расчетной ставке 10/110'

    VAT120 = 'vat120'
    'НДС чека по расчетной ставке 20/120'


class DocumentCode(Enum):
    """Числовой код вида документа, удостоверяющего личность."""

    PASSPORT_RF = 21
    """Паспорт гражданина Российской Федерации"""

    PASSPORT_RF_INTERNATIONAL = 22
    """
    Паспорт гражданина Российской Федерации, дипломатический паспорт, служебный
    паспорт, удостоверяющие личность гражданина Российской Федерации за
    пределами Российской Федерации
    """

    TEMP_ID_RF = 26
    """
    Временное удостоверение личности гражданина Российской Федерации,
    выдаваемое на период оформления паспорта гражданина Российской Федерации
    """

    BIRTH_CERTIFICATE_RF = 27
    """
    Свидетельство о рождении гражданина Российской Федерации — для граждан
    Российской Федерации в возрасте до 14 лет
    """

    OTHER_RF_ID = 28
    """
    Иные документы, признаваемые документами, удостоверяющими личность
    гражданина Российской Федерации в соответствии с законодательством
    Российской Федерации
    """

    FOREIGN_PASSPORT = 31
    """Паспорт иностранного гражданина"""

    OTHER_FOREIGN_ID = 32
    """
    Иные документы, признаваемые документами, удостоверяющими личность
    иностранного гражданина в соответствии с законодательством Российской
    Федерации и международным договором Российской Федерации
    """

    STATELESS_DOC = 33
    """
    Документ, выданный иностранным государством и признаваемый в соответствии
    с международным договором Российской Федерации в качестве документа,
    удостоверяющего личность лица безгражданства.
    """

    RESIDENCE_PERMIT = 34
    """Вид на жительство — для лиц без гражданства"""

    TEMPORARY_RESIDENCE = 35
    """Разрешение на временное проживание — для лиц без гражданства"""

    ASYLUM_REQUEST = 36
    """
    Свидетельство о рассмотрении ходатайства о признании лица без гражданства
    беженцем на территории Российской Федерации по существу
    """

    REFUGEE_ID = 37
    """Удостоверение беженца"""

    OTHER_STATELESS_ID = 38
    """
    Иные документы, признаваемые документами, удостоверяющими личность лиц без
    гражданства в соответствии с законодательством Российской Федерации и
    международным договором Российской Федерации
    """

    NO_ID_DOC = 40
    """
    Документ, удостоверяющий личность лица, не имеющего действительного
    документа, удостоверяющего личность, на период рассмотрения заявления о
    признании гражданином Российской Федерации или о приеме в гражданство
    Российской Федерации
    """


class PaymentObject(StrEnum):
    """Значения реквизита «признак предмета расчета» — тег 1212, таблица 101"""

    COMMODITY = 'commodity'
    """Товар"""

    EXCISE = 'excise'
    """Подакцизный товар"""

    JOB = 'job'
    """Работа"""

    SERVICE = 'service'
    """Услуга"""

    GAMBLING_BET = 'gambling_bet'
    """Ставка азартной игры"""

    GAMBLING_PRIZE = 'gambling_prize'
    """Выигрыш азартной игры"""

    LOTTERY = 'lottery'
    """Лотерейный билет"""

    LOTTERY_PRIZE = 'lottery_prize'
    """Выигрыш лотереи"""

    INTELLECTUAL_ACTIVITY = 'intellectual_activity'
    """Предоставление, результатов интеллектуальной деятельности"""

    PAYMENT = 'payment'
    """Платеж"""

    AGENT_COMMISSION = 'agent_commission'
    """Агентское вознаграждение"""

    CONTRIBUTION = 'contribution'
    """Выплата"""

    PROPERTY_RIGHTS = 'property_rights'
    """Имущественное право"""

    UNREALIZATION = 'unrealization'
    """Внереализационный доход"""

    TAX_REDUCTION = 'tax_reduction'
    """Иные платежи и взносы"""

    TRADE_FEE = 'trade_fee'
    """Торговый сбор"""

    RESORT_TAX = 'resort_tax'
    """Курортный сбор"""

    PLEDGE = 'pledge'
    """Залог"""

    INCOME_DECREASE = 'income_decrease'
    """Расход"""

    IE_PENSION_INSURANCE_WITHOUT_PAYMENTS = (
        'ie_pension_insurance_without_payments'
    )
    """Взносы на ОПС ИП"""

    IE_PENSION_INSURANCE_WITH_PAYMENTS = 'ie_pension_insurance_with_payments'
    """Взносы на ОПС"""

    IE_MEDICAL_INSURANCE_WITHOUT_PAYMENTS = (
        'ie_medical_insurance_without_payments'
    )
    """Взносы на ОМС ИП"""

    IE_MEDICAL_INSURANCE_WITH_PAYMENTS = 'ie_medical_insurance_with_payments'
    """Взносы на ОМС"""

    SOCIAL_INSURANCE = 'social_insurance'
    """Взносы на ОСС"""

    CASINO_CHIPS = 'casino_chips'
    """Платеж казино"""

    AGENT_PAYMENT = 'agent_payment'
    """Выдача ДС"""

    EXCISABLE_GOODS_WITHOUT_MARKING_CODE = (
        'excisable_goods_without_marking_code'
    )
    """АТНМ"""

    EXCISABLE_GOODS_WITH_MARKING_CODE = 'excisable_goods_with_marking_code'
    """АТМ"""

    GOODS_WITHOUT_MARKING_CODE = 'goods_without_marking_code'
    """ТНМ"""

    GOODS_WITH_MARKING_CODE = 'goods_with_marking_code'
    """ТМ"""

    ANOTHER = 'another'
    """Иной предмет расчета"""


class MeasurementUnit(Enum):
    """Единицы измерения."""

    PIECE = 0
    """шт. или ед."""

    GRAM = 10
    """г"""

    KILOGRAM = 11
    """кг"""

    TON = 12
    """т"""

    CENTIMETER = 20
    """см"""

    DECIMETER = 21
    """дм"""

    METER = 22
    """м"""

    SQUARE_CENTIMETER = 30
    """кв. см"""

    SQUARE_DECIMETER = 31
    """кв. дм"""

    SQUARE_METER = 32
    """кв. м"""

    MILLILITER = 40
    """мл"""

    LITER = 41
    """л"""

    CUBIC_METER = 42
    """куб. м"""

    KILOWATT_HOUR = 50
    """кВт·ч"""

    GIGACALORIE = 51
    """Гкал"""

    DAY = 70
    """сутки"""

    HOUR = 71
    """час"""

    MINUTE = 72
    """мин"""

    SECOND = 73
    """с"""

    KILOBYTE = 80
    """Кбайт"""

    MEGABYTE = 81
    """Мбайт"""

    GIGABYTE = 82
    """Гбайт"""

    TERABYTE = 83
    """Тбайт"""

    OTHER = 255
    """Иные единицы измерения"""
