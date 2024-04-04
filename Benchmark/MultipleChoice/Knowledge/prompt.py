"""PROMPT POOL THAT HAS BEEN USED FOR Multiple Choice EVALUATION"""

ENGLISH_ZERO = """
  In this task, you will be presented with a multiple-choice question in Persian, and you should answer the question based on your knowledge. choose the answer from the given candidates.

  question:
  '''{question}'''
  
  candidates:
  '''[{candidates}]'''

  answer:
  """

PERSIAN_ZERO = """
  در ادامه، به شما یک سوال چند گزینه‌ای به زبان فارسی نشان داده می شود. شما باید بر اساس دانش خود به سوال پاسخ دهید. پاسخ خود را از بین گزینه‌های داده شده انتخاب کنید.

  سوال:
  '''{question}'''

  گزینه ها:
  '''[{candidates}]'''

  جواب:
"""


ENGLISH_ONE = """
  In this task, you will be presented with a multiple-choice question in Persian, and you should answer the question based on your knowledge. choose the answer from the given candidates.

  sample:

  question:
  وسیع ترین کشور جهان کدام است؟

  candidtaes:
  [آمریکا,کانادا,روسیه,چین]

  answer:
  روسیه

  question:
  '''{question}'''

  candidates:
  '''[{candidates}]'''

  answer:
  """

PERSIAN_ONE = """
  در ادامه، به شما یک سوال چند گزینه‌ای به زبان فارسی نشان داده می شود. شما باید بر اساس دانش خود به سوال پاسخ دهید. پاسخ خود را از بین گزینه‌های داده شده انتخاب کنید.

  نمونه:

  سوال:
  وسیع ترین کشور جهان کدام است؟

  گزینه ها:
  [آمریکا,کانادا,روسیه,چین]

  جواب:
  روسیه

  سوال:
  '''{question}'''

  گزینه ها:
  '''[{candidates}]'''

  جواب:
"""

ENGLISH_THREE = """
  In this task, you will be presented with a multiple-choice question in Persian, and you should answer the question based on your knowledge. choose the answer from the given candidates.

  sample:

  question:
  کدام یک از موارد زیر، عکس جریان ارتباط اصلی است و طی آن گیرنده پیام جدیدی را می فرستد؟

  candidtaes:
  [ورود عوامل مزاحم, کد گذاری,استفاده از نماد,بازخورد ]

  answer:
  بازخورد 

  question:
  برنامه های عمرانی کشور چگونه است؟

  candidtaes:
  [بلند مدت,کوتاه مدت,میان مدت,بلند مدت و میان مدت]

  answer:
  میان مدت

  question:
  حکومت قاجار در چه سالی به پایان رسید؟

  candidtaes:
  [۱۳۰۷ ش,۱۳۲۰ ش,۱۳۱۷ ش,۱۳۰۴ ش]

  answer:
  ۱۳۰۴ ش

  question:
  '''{question}'''

  candidates:
  '''[{candidates}]'''

  answer:
  """

PERSIAN_THREE = """
  در ادامه، به شما یک سوال چند گزینه‌ای به زبان فارسی نشان داده می شود. شما باید بر اساس دانش خود به سوال پاسخ دهید. پاسخ خود را از بین گزینه‌های داده شده انتخاب کنید.

  نمونه:

  سوال:
  کدام یک از موارد زیر، عکس جریان ارتباط اصلی است و طی آن گیرنده پیام جدیدی را می فرستد؟

  گزینه ها:
  [ورود عوامل مزاحم, کد گذاری,استفاده از نماد,بازخورد ]

  جواب:
  بازخورد 

  سوال:
  برنامه های عمرانی کشور چگونه است؟

  گزینه ها:
  [بلند مدت,کوتاه مدت,میان مدت,بلند مدت و میان مدت]

  جواب:
  میان مدت

  سوال:
  حکومت قاجار در چه سالی به پایان رسید؟

  گزینه ها:
  [۱۳۰۷ ش,۱۳۲۰ ش,۱۳۱۷ ش,۱۳۰۴ ش]

  جواب:
  ۱۳۰۴ ش

  سوال:
  '''{question}'''

  گزینه ها:
  '''[{candidates}]'''

  جواب:
"""
