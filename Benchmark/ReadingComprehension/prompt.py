"""PROMPT POOL THAT HAS BEEN USED FOR Reading Comprehension EVALUATION"""

ENGLISH_ZERO = """
  In this task, you will be shown a Persian passage and question. You need to write an answer for the question. Try to keep your answers as short as possible.

  context:
  '''{context}'''

  question:
  '''{question}'''

  answer:
  """

PERSIAN_ZERO = """
  در ادامه به شما یک متن فارسی و یک سوال نشان داده می شود. شما باید برای سوال یک پاسخ بنویسید. سعی کنید پاسخ های خود را تا حد ممکن کوتاه بدهید.

  متن:
  '''{context}'''

  سوال:
  '''{question}'''

  جواب:
  """

ENGLISH_ONE = """
  In this task, you will be shown a Persian passage and question. You need to write a answer for the question. Try to keep your answers as short as possible.

  sample:

  question:
  ویتامین ای را چه موقع استفاده کنیم؟

  answer:
  برای رفع چین و چروک پیشانی و دیگر نشانه های پیری

  context:
  '''{context}'''

  question:
  '''{question}'''

  answer:
  """

PERSIAN_ONE = """
  در ادامه به شما یک متن فارسی و یک سوال نشان داده می شود. شما باید برای سوال یک پاسخ بنویسید. سعی کنید پاسخ های خود را تا حد ممکن کوتاه بدهید.

  نمونه:

  سوال:
  ویتامین ای را چه موقع استفاده کنیم؟

  جواب:
  برای رفع چین و چروک پیشانی و دیگر نشانه های پیری

  متن:
  '''{context}'''

  سوال:
  '''{question}'''

  جواب:
  """

ENGLISH_THREE = """
  In this task, you will be shown a Persian passage and question. You need to write a answer for the question. Try to keep your answers as short as possible.

  samples:

  question:
  ویتامین ای را چه موقع استفاده کنیم؟

  answer:
  برای رفع چین و چروک پیشانی و دیگر نشانه های پیری

  question:
  چرا نام برج میلاد میلاد است؟

  answer:
  به مناسبت یکصدمین زادروز روح‌الله خمینی بنیان‌گذار جمهوری اسلامی ایران

  question:
  متفقین به کدام کشور لقب پل پیروزی دادند؟

  answer:
  ایران

  context:
  '''{context}'''

  question:
  '''{question}'''

  answer:
  """

PERSIAN_THREE = """
  در ادامه به شما یک متن فارسی و یک سوال نشان داده می شود. شما باید برای سوال یک پاسخ بنویسید. سعی کنید پاسخ های خود را تا حد ممکن کوتاه بدهید.

  نمونه:

  سوال:
  ویتامین ای را چه موقع استفاده کنیم؟

  جواب:
  برای رفع چین و چروک پیشانی و دیگر نشانه های پیری

  سوال:
  چرا نام برج میلاد میلاد است؟

  جواب:
  به مناسبت یکصدمین زادروز روح‌الله خمینی بنیان‌گذار جمهوری اسلامی ایران

  سوال:
  متفقین به کدام کشور لقب پل پیروزی دادند؟

  جواب:
  ایران

  متن:
  '''{context}'''

  سوال:
  '''{question}'''

  جواب:
  """