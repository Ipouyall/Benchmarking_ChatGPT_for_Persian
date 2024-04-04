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
  حاصل عبارت ۴ + ۵۵۳ برابر است با ؟

  candidtaes:
  [558,557,556,554]

  answer:
  557

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
  حاصل عبارت ۴ + ۵۵۳ برابر است با ؟

  گزینه ها:
  [558,557,556,554]

  جواب:
  557

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
  شعاع دایره اي یک دهم افزایش یافته است. مساحت مربع محاطی آن چند درصد افزایش مییابد؟

  candidtaes:
  [۷۹,۲۱,۱۹,۸۱]

  answer:
  ۲۱

  question:
  %40 عدد 100 برابر است با ....

  candidtaes:
  [30,40,50,60]

  answer:
  40

  question:
  حاصل عبارت ۴ + ۵ برابر است با ؟

  candidtaes:
  [9,10,11,8]

  answer:
  9

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
  شعاع دایره اي یک دهم افزایش یافته است. مساحت مربع محاطی آن چند درصد افزایش مییابد؟

  گزینه ها:
  [۷۹,۲۱,۱۹,۸۱]

  جواب:
  ۲۱

  سوال:
  %40 عدد 100 برابر است با ....

  گزینه ها:
  [30,40,50,60]

  جواب:
  40

  سوال:
  حاصل عبارت ۴ + ۵ برابر است با ؟

  گزینه ها:
  [9,10,11,8]

  جواب:
  9

  سوال:
  '''{question}'''

  گزینه ها:
  '''[{candidates}]'''

  جواب:
"""
