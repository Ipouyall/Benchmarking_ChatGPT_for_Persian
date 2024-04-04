

ENGLISH_ZERO = """
  Task Description:
  In this task, which is Machine Translation (MT), you will be presented with a sentence in {source_language}.
  You should translate it to {target_language} in the most appropriate way.

  Input:
  {input}
  """

PERSIAN_ZERO = """
  شرح وظیفه:
  در ادامه‌، وظیفه‌ (تکلیفی) برای شما درنظر گرفته شده است، که مربوط به ترجمه ماشینی است.
  به این منظور جمله‌ای به زبان {source_language} به شما نشان داده می‌شود  
  در نتیجه، شما باید آن جمله را به شکل مناسب و دقیق به زبان {target_language} ترجمه کنید.

  ورودی:
  {input}

  """

ENGLISH_ONE = """
  Task Description:
  In this task, which is Machine Translation (MT), you will be presented with a sentence in {source_language}.
  You should translate it to {target_language} in the most appropriate way.

  Here is an example for this task, which is translating sentences from {source_language} to {target_language}:
  'This is a sample sentence that we are going to translate it.'
  -> 'این یک جمله‌ی نمونه است که می‌خواهیم آن را ترجمه کنیم.'

  Input:
  {input}
  """

PERSIAN_ONE = """
  شرح وظیفه:
  در ادامه‌، وظیفه‌ (تکلیفی) برای شما درنظر گرفته شده است، که مربوط به ترجمه ماشینی است.
  به این منظور جمله‌ای به زبان {source_language} به شما نشان داده می‌شود  
  در نتیجه، شما باید آن جمله را به شکل مناسب و دقیق به زبان {target_language} ترجمه کنید.

  مثالی از ترجمه‌ی جمله‌ی نمونه از زبان {source_language} به {target_language}:
  'This is a sample sentence that we are going to translate it.'
  -> 'این یک جمله‌ی نمونه است که می‌خواهیم آن را ترجمه کنیم.'

  ورودی:
  {input}
  """

ENGLISH_THREE = """
  Task Description:
  In this task, which is Machine Translation (MT), you will be presented with a sentence in {source_language}.
  You should translate it to {target_language} in the most appropriate way.
  
  Here are some examples for this task, which is translating sentences from {source_language} to {target_language}:
  'I love programming.'
  -> ' من برنامه‌نویسی را دوست دارم.'
  'Cooking a delicious meal requires a combination of ingredients and techniques.'
  -> 'پخت یک وعده غذای خوشمزه نیازمند ترکیبی از مواد اولیه و تکنیک‌هاست.'
  'In the realm of artificial intelligence, neural networks play a pivotal role.'
  -> 'در دنیای هوش مصنوعی، شبکه‌های عصبی نقشی کلیدی ایفا می‌کنند.'

  Input:
  {input}
  """

PERSIAN_THREE = """
  شرح وظیفه:
  در ادامه‌، وظیفه‌ (تکلیفی) برای شما درنظر گرفته شده است، که مربوط به ترجمه ماشینی است.
  به این منظور جمله‌ای به زبان {source_language} به شما نشان داده می‌شود  
  در نتیجه، شما باید آن جمله را به شکل مناسب و دقیق به زبان {target_language} ترجمه کنید.

  مثال‌هایی از ترجمه‌ی جملات نمونه از زبان {source_language} به {target_language}:
  'I love programming.'
  ->'من برنامه‌نویسی را دوست دارم.'
  'Cooking a delicious meal requires a combination of ingredients and techniques.'
  -> 'پخت یک وعده غذای خوشمزه نیازمند ترکیبی از مواد اولیه و تکنیک‌هاست.'
  'In the realm of artificial intelligence, neural networks play a pivotal role.'
  -> 'در دنیای هوش مصنوعی، شبکه‌های عصبی نقشی کلیدی ایفا می‌کنند.'

  ورودی:
  {input}
  """