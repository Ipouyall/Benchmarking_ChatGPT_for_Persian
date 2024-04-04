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
  در کدام گزینه، آثار موسوی گرما رودی تماما درست است؟

  candidtaes:
  [سرود رگبار، دستچين، عبور، چمن لاله,چمن لاله، خطّ خون، مثل درخت در شب باران، سرود رگبار,در سايه سار نخل ولايت، از بودن و سرودن، خطّ خون، عبور,تاناكجا، دستچين، در سايه سار نخل ولايت، از بودن و سرودن]

  answer:
  سرود رگبار، دستچين، عبور، چمن لاله

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
  در کدام گزینه، آثار موسوی گرما رودی تماما درست است؟

  گزینه ها:
  [سرود رگبار، دستچين، عبور، چمن لاله,چمن لاله، خطّ خون، مثل درخت در شب باران، سرود رگبار,در سايه سار نخل ولايت، از بودن و سرودن، خطّ خون، عبور,تاناكجا، دستچين، در سايه سار نخل ولايت، از بودن و سرودن]

  جواب:
  سرود رگبار، دستچين، عبور، چمن لاله

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
  در عيد .   .   . دين اسلام كامل شد.

  candidtaes:
  [عيد فطر,عيد قربان,عيد مبعث,عيد غدير]

  answer:
  عيد غدير

  question:
  کدام گزینه ازموضوعات شعری عصررودکی نیست؟

  candidtaes:
  [وصف,عرفان,مدح,اندرز]

  answer:
  عرفان

  question:
  آنچه که از ارزش واقعی چیزی بکاهد :؟

  candidtaes:
  [انتقاد,شایعه,فراوانی,نقص]

  answer:
  نقص

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
  در عيد .   .   . دين اسلام كامل شد.

  گزینه ها:
  [عيد فطر,عيد قربان,عيد مبعث,عيد غدير]

  جواب:
  عيد غدير

  سوال:
  کدام گزینه ازموضوعات شعری عصررودکی نیست؟

  گزینه ها:
  [وصف,عرفان,مدح,اندرز]

  جواب:
  عرفان

  سوال:
  آنچه که از ارزش واقعی چیزی بکاهد :؟

  گزینه ها:
  [انتقاد,شایعه,فراوانی,نقص]

  جواب:
  نقص

  سوال:
  '''{question}'''

  گزینه ها:
  '''[{candidates}]'''

  جواب:
"""
