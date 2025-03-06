from enum import Enum, StrEnum


class PayType(StrEnum):
    ONE = 'O'
    TWO = 'T'


class Language(StrEnum):
    RU = 'ru'
    EN = 'en'


class Taxation(StrEnum):
    OSN = 'osn'
    USN_INCOME = 'usn_income'
    USN_INCOME_OUTCOME = 'usn_income_outcome'
    ENVD = 'envd'
    ESN = 'esn'
    PATENT = 'patent'


class PaymentObject_FFD_12(StrEnum):
    COMMODITY = 'commodity'
    EXCISE = 'excise'
    JOB = 'job'
    SERVICE = 'service'
    GAMBLING_BET = 'gambling_bet'
    GAMBLING_PRIZE = 'gambling_prize'
    LOTTERY = 'lottery'
    LOTTERY_PRIZE = 'lottery_prize'
    INTELLECTUAL_ACTIVITY = 'intellectual_activity'
    PAYMENT = 'payment'
    AGENT_COMMISSION = 'agent_commission'
    CONTRIBUTION = 'contribution'
    PROPERTY_RIGHTS = 'property_rights'
    UNREALIZATION = 'unrealization'
    TAX_REDUCTION = 'tax_reduction'
    TRADE_FEE = 'trade_fee'
    RESORT_TAX = 'resort_tax'
    PLEDGE = 'pledge'
    INCOME_DECREASE = 'income_decrease'
    IE_PENSION_INSURANCE_WITHOUT_PAYMENTS = (
        'ie_pension_insurance_without_payments'
    )
    IE_PENSION_INSURANCE_WITH_PAYMENTS = 'ie_pension_insurance_with_payments'
    IE_MEDICAL_INSURANCE_WITHOUT_PAYMENTS = (
        'ie_medical_insurance_without_payments'
    )
    IE_MEDICAL_INSURANCE_WITH_PAYMENTS = 'ie_medical_insurance_with_payments'
    SOCIAL_INSURANCE = 'social_insurance'
    CASINO_CHIPS = 'casino_chips'
    AGENT_PAYMENT = 'agent_payment'
    EXCISABLE_GOODS_WITHOUT_MARKING_CODE = (
        'excisable_goods_without_marking_code'
    )
    EXCISABLE_GOODS_WITH_MARKING_CODE = 'excisable_goods_with_marking_code'
    GOODS_WITHOUT_MARKING_CODE = 'goods_without_marking_code'
    GOODS_WITH_MARKING_CODE = 'goods_with_marking_code'
    ANOTHER = 'another'


class PaymentObject_FFD_105(StrEnum):
    COMMODITY = 'commodity'
    EXCISE = 'excise'
    JOB = 'job'
    SERVICE = 'service'
    GAMBLING_BET = 'gambling_bet'
    GAMBLING_PRIZE = 'gambling_prize'
    LOTTERY = 'lottery'
    LOTTERY_PRIZE = 'lottery_prize'
    INTELLECTUAL_ACTIVITY = 'intellectual_activity'
    PAYMENT = 'payment'
    AGENT_COMMISSION = 'agent_commission'
    COMPOSITE = 'composite'
    ANOTHER = 'another'


class Tax(StrEnum):
    NONE = 'none'
    VAT0 = 'vat0'
    VAT5 = 'vat5'
    VAT7 = 'vat7'
    VAT10 = 'vat10'
    VAT20 = 'vat20'
    VAT105 = 'vat105'
    VAT107 = 'vat107'
    VAT110 = 'vat110'
    VAT120 = 'vat120'


class AgentSign(StrEnum):
    BANK_PAYING_AGENT = 'bank_paying_agent'
    BANK_PAYING_SUBAGENT = 'bank_paying_subagent'
    PAYING_AGENT = 'paying_agent'
    PAYING_SUBAGENT = 'paying_subagent'
    ATTORNEY = 'attorney'
    COMMISSION_AGENT = 'commission_agent'
    ANOTHER = 'another'


class DocumentСode(Enum):
    PASSPORT_RF = 21  # Паспорт гражданина Российской Федерации
    PASSPORT_RF_INTERNATIONAL = 22  # Паспорт РФ (дипломатический, служебный)
    TEMP_ID_RF = 26  # Временное удостоверение личности РФ
    BIRTH_CERTIFICATE_RF = 27  # Свидетельство о рождении (до 14 лет)
    OTHER_RF_ID = 28  # Иные документы, удостоверяющие личность РФ
    FOREIGN_PASSPORT = 31  # Паспорт иностранного гражданина
    OTHER_FOREIGN_ID = 32  # Иные документы иностранного гражданина
    STATELESS_DOC_FOREIGN = 33  # Документ лица без гражданства (иностранный)
    RESIDENCE_PERMIT = 34  # Вид на жительство (лица без гражданства)
    # Разрешение на временное проживание (лица без гражданства)
    TEMP_RESIDENCE_PERMIT = 35
    # Свидетельство о рассмотрении ходатайства о беженстве
    ASYLUM_REQUEST_CERTIFICATE = 36
    REFUGEE_ID = 37  # Удостоверение беженца
    OTHER_STATELESS_ID = 38  # Иные документы лиц без гражданства
    TEMP_CITIZENSHIP_ID = 40  # Документ на период рассмотрения гражданства РФ


class PaymentMethod(StrEnum):
    FULL_PREPAYMENT = 'full_prepayment'
    PREPAYMENT = 'prepayment'
    ADVANCE = 'advance'
    FULL_PAYMENT = 'full_payment'
    PARTIAL_PAYMENT = 'partial_payment'
    CREDIT = 'credit'
    CREDIT_PAYMENT = 'credit_payment'


class MeasurementUnit(Enum):
    PIECE = '0'  # шт. или ед.
    GRAM = '10'  # г
    KILOGRAM = '11'  # кг
    TON = '12'  # т
    CENTIMETER = '20'  # см
    DECIMETER = '21'  # дм
    METER = '22'  # м
    SQUARE_CM = '30'  # кв. см
    SQUARE_DM = '31'  # кв. дм
    SQUARE_M = '32'  # кв. м
    MILLILITER = '40'  # мл
    LITER = '41'  # л
    CUBIC_M = '42'  # куб. м
    KWH = '50'  # кВт · ч
    GIGACALORIE = '51'  # Гкал
    DAY = '70'  # сутки
    HOUR = '71'  # час
    MINUTE = '72'  # мин
    SECOND = '73'  # с
    KILOBYTE = '80'  # Кбайт
    MEGABYTE = '81'  # Мбайт
    GIGABYTE = '82'  # Гбайт
    TERABYTE = '83'  # Тбайт
    OTHER = '255'  # Иные единицы измерения


class MarkCodeType(StrEnum):
    UNKNOWN = 'UNKNOWN'
    EAN8 = 'EAN8'
    EAN13 = 'EAN1'
    ITF14 = 'ITF14'
    GS10 = 'GS10'
    GS1M = 'GS1M'
    SHORT = 'SHORT'
    FUR = 'FUR'
    EGAIS20 = 'EGAIS20'
    EGAIS30 = 'EGAIS30'
    RAWCODE = 'RAWCODE'


class OperationInitiatorType(StrEnum):
    CIT_CREDENTIAL_NOT_CAPTURED = '0'  # Оплата без сохранения реквизитов карты
    CONSUMER_INITIATED_CREDENTIAL_CAPTURED = '1'  # Мерчант сохраняет карту
    # Операция по сохранённой карте, инициирована клиентом
    CONSUMER_INITIATED_CREDENTIAL_ON_FILE = '2'
    # Повторяющаяся операция без графика (Merchant-Initiated)
    MERCHANT_INITIATED_RECURRING = 'R'
    # Повторяющаяся операция по графику (Merchant-Initiated)
    MERCHANT_INITIATED_INSTALLMENT = 'I'


class Device(StrEnum):
    SDK = 'SDK'
    DESKTOP = 'Desktop'
    MOBILE_WEB = 'MobileWeb'


class TicketRestriction(Enum):
    NO_RESTRICTIONS = '0'  # Без ограничений
    NON_REFUNDABLE = '1'  # Невозвратный
