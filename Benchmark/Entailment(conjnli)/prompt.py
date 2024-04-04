"""PROMPT POOL THAT HAS BEEN USED FOR Entailment(conjnli) EVALUATION"""

ENGLISH_ZERO = """
    You will be presented with a premise, and a hypothesis about that premise. /
    You need to decide whether the hypothesis is entailed by the premise by choosing one of the following answers: /
    'e': The hypothesis follows logically from the information contained in the premise. /
    'c': The hypothesis is logically false from the information contained in the premise. /
    'n': It is not possible to determine whether the hypothesis is true or false without further information./
    Read the passage of information thoroughly and select the correct answer from the three answer labels. /
    Read the premise thoroughly to ensure you know what the premise entails.

    premise:
    '''{premise}'''
    hypothesis:
    '''{hypothesis}'''
    answer:

    """


PERSIAN_ZERO = """\
    به شما یک پیش فرض و یک فرضیه در مورد آن پیش فرض ارائه می شود. 
     شما باید با انتخاب یکی از پاسخ های زیر تصمیم بگیرید که آیا فرضیه مستلزم پیش فرض است:
     'e': فرضیه به طور منطقی از اطلاعات موجود در پیش فرض ناشی می شود. 
     'c': فرضیه از نظر منطقی از اطلاعات موجود در پیش فرض نادرست است. 
     'n': تشخیص درست یا نادرست بودن فرضیه بدون اطلاعات بیشتر ممکن نیست.
     قسمت اطلاعات را به طور کامل بخوانید و از بین سه برچسب پاسخ، پاسخ صحیح را انتخاب کنید. 
     پیش فرض را به طور کامل بخوانید تا مطمئن شوید که پیش فرض را شامل می شود.
    
    پیش فرض:
    '''{premise}'''
    فرضیه:
    '''{hypothesis}'''
    پاسخ:\

"""

ENGLISH_ONE = """
    You will be presented with a premise, and a hypothesis about that premise. /
    You need to decide whether the hypothesis is entailed by the premise by choosing one of the following answers: /
    'e': The hypothesis follows logically from the information contained in the premise. /
    'c': The hypothesis is logically false from the information contained in the premise. /
    'n': It is not possible to determine whether the hypothesis is true or false without further information./
    Read the passage of information thoroughly and select the correct answer from the three answer labels. /
    Read the premise thoroughly to ensure you know what the premise entails.

    premise:
    مهاجران آفریقایی در اروپا در آفریقا متولد می شوند اما در اروپا زندگی می کنند.
    hypothesis:
    مهاجران آفریقایی در اروپا یا در آفریقا به دنیا آمده اند یا از نژاد آفریقایی هستند اما در اروپا زندگی می کنند.
    answer:
    'e'

    premise:
    '''{premise}'''
    hypothesis:
    '''{hypothesis}'''
    answer:

    """


PERSIAN_ONE = """
    به شما یک پیش فرض و یک فرضیه در مورد آن پیش فرض ارائه می شود. /
     شما باید با انتخاب یکی از پاسخ های زیر تصمیم بگیرید که آیا فرضیه مستلزم پیش فرض است:
     'e': فرضیه به طور منطقی از اطلاعات موجود در پیش فرض ناشی می شود. /
     'c': فرضیه از نظر منطقی از اطلاعات موجود در پیش فرض نادرست است. /
     'n': تشخیص درست یا نادرست بودن فرضیه بدون اطلاعات بیشتر ممکن نیست./
     قسمت اطلاعات را به طور کامل بخوانید و از بین سه برچسب پاسخ، پاسخ صحیح را انتخاب کنید. /
     پیش فرض را به طور کامل بخوانید تا مطمئن شوید که پیش فرض را شامل می شود.

    پیش فرض:
    مهاجران آفریقایی در اروپا در آفریقا متولد می شوند اما در اروپا زندگی می کنند.
    فرضیه:
    مهاجران آفریقایی در اروپا یا در آفریقا به دنیا آمده اند یا از نژاد آفریقایی هستند اما در اروپا زندگی می کنند.
    پاسخ:
    'e'

    پیش فرض:
    '''{premise}'''
    فرضیه:
    '''{hypothesis}'''
    پاسخ:

"""


ENGLISH_THREE = """
    You will be presented with a premise, and a hypothesis about that premise. /
    You need to decide whether the hypothesis is entailed by the premise by choosing one of the following answers: /
    'e': The hypothesis follows logically from the information contained in the premise. /
    'c': The hypothesis is logically false from the information contained in the premise. /
    'n': It is not possible to determine whether the hypothesis is true or false without further information./
    Read the passage of information thoroughly and select the correct answer from the three answer labels. /
    Read the premise thoroughly to ensure you know what the premise entails.

    premise:
    نام چینی مجازی است، نه تحت اللفظی، زیرا در این غذا نه چای و نه سوپی وجود دارد.
    hypothesis:
    نام چینی مجازی است نه تحت اللفظی، زیرا در این غذا چای وجود دارد .
    answer:
    'c'

    premise:
    برای کشت در باغ آلپینیوم مناسب است.
    hypothesis:
    برای کشت در باغ آلپینیوم یا باغ صخره ای مناسب است.
    answer:
    'n'

    premise:
    مهاجران آفریقایی در اروپا در آفریقا متولد می شوند اما در اروپا زندگی می کنند.
    hypothesis:
    مهاجران آفریقایی در اروپا یا در آفریقا به دنیا آمده اند یا از نژاد آفریقایی هستند اما در اروپا زندگی می کنند.
    answer:
    'e'

    premise:
    '''{premise}'''
    hypothesis:
    '''{hypothesis}'''
    answer:

    """


PERSIAN_THREE = """
    به شما یک پیش فرض و یک فرضیه در مورد آن پیش فرض ارائه می شود. /
     شما باید با انتخاب یکی از پاسخ های زیر تصمیم بگیرید که آیا فرضیه مستلزم پیش فرض است:
     'e': فرضیه به طور منطقی از اطلاعات موجود در پیش فرض ناشی می شود. /
     'c': فرضیه از نظر منطقی از اطلاعات موجود در پیش فرض نادرست است. /
     'n': تشخیص درست یا نادرست بودن فرضیه بدون اطلاعات بیشتر ممکن نیست./
     قسمت اطلاعات را به طور کامل بخوانید و از بین سه برچسب پاسخ، پاسخ صحیح را انتخاب کنید. /
     پیش فرض را به طور کامل بخوانید تا مطمئن شوید که پیش فرض را شامل می شود.

    پیش فرض:
    نام چینی مجازی است، نه تحت اللفظی، زیرا در این غذا نه چای و نه سوپی وجود دارد.
    فرضیه:
    نام چینی مجازی است نه تحت اللفظی، زیرا در این غذا چای وجود دارد .
    پاسخ:
    'c'

    پیش فرض:
    برای کشت در باغ آلپینیوم مناسب است.
    فرضیه:
    برای کشت در باغ آلپینیوم یا باغ صخره ای مناسب است.
    پاسخ:
    'n'

    پیش فرض:
    مهاجران آفریقایی در اروپا در آفریقا متولد می شوند اما در اروپا زندگی می کنند.
    فرضیه:
    مهاجران آفریقایی در اروپا یا در آفریقا به دنیا آمده اند یا از نژاد آفریقایی هستند اما در اروپا زندگی می کنند.
    پاسخ:
    'e'

    پیش فرض:
    '''{premise}'''
    فرضیه:
    '''{hypothesis}'''
    پاسخ:

"""

