from enum import Enum


class SentenceEnum(Enum):
    Initial = 1
    Saved = 2
    Processing = 3
    Completed = 4


class SuggestEnum(Enum):
    Waiting = 1
    Accept = 2
    Reject = 3


class JudgmentEnum(Enum):
    Saved = 1
    Processed = 2
    Rejected = 3


class PaymentEnum(Enum):
    payed = 1




