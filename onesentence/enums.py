from enum import Enum


class SentenceEnum(Enum):
    Initial = 1  # ثبت اولیه
    Saved = 2  # ثبت نهایی
    Processing = 3  # در حال انجام
    Completed = 4  # تحویل شده


class SuggestEnum(Enum):
    Waiting = 1  # منتظر بررسی
    Accept = 2  # تایید پیشنهاد
    Reject = 3  # رد شده


class JudgmentEnum(Enum):
    Saved = 1  # ثبت شده
    Processed = 2  # بررسی شده
    Rejected = 3  # رد شده


class PaymentEnum(Enum):
    payed = 1  # پرداخت شد


class UserStatusEnum(Enum):
    Active = 1  # فعال
    DeActive = 2  # غیرفعال


class UserTypeEnum(Enum):
    Applicator = 1  # درخواست کننده
    Translator = 2  # مترجم
