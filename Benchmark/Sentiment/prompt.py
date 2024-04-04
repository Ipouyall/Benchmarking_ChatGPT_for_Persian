"""PROMPT POOL THAT HAS BEEN USED FOR SENTIMENT ANALYSIS"""

ENGLISH_ZERO = """\
The below sentence is a person's review. The review is in Persian. Identify the sentiment or polarity associated with it.
Possible answers are: POSITIVE, NEUTRAL, NEGATIVE, OTHER.
Use OTHER when the sentence does not include any specific sense, or has mixed or borderline senses.

Review: {review}
Sentiment: 
"""

ENGLISH_ONE = '''\
The below sentence is a person's review. The review is in Persian. Identify the sentiment or polarity associated with it.
Possible answers are: POSITIVE, NEUTRAL, NEGATIVE, OTHER.
Use OTHER when the sentence does not include any specific sense, or has mixed or borderline senses.

Examples:

Example 1:
Review: طعم بد . بوی بد . فقط قیمتش خوبه .
Sentiment: NEGATIVE

Example 2:
Review: با بقیه چایی ها هیچ فرقی نداره چه طعم چه رنگ
Sentiment: NEUTRAL

Example 3:
Review: خوب بود و در باز بودن و طعم خوبی داشت
Sentiment: POSITIVE

Example 4:
Review: مزه اش یه جور خاصه تند تند نیس ولی متفاوته
Sentiment: OTHER

Review: {review}
Sentiment: 
'''

ENGLISH_THREE = """\
The below sentence is a person's review. The review is in Persian. Identify the sentiment or polarity associated with it.
Possible answers are: POSITIVE, NEUTRAL, NEGATIVE, OTHER.
Use OTHER when the sentence does not include any specific sense, or has mixed or borderline senses.

Examples:

Example 1:
Review: طعم بد . بوی بد . فقط قیمتش خوبه .
Sentiment: NEGATIVE

Example 2:
Review: بعد از ۵ دقیقه مزه اش رو از دست میده
Sentiment: NEGATIVE

Example 3:
Review: طرفش خیلی نازکه تو دست نمیشه نگه داشت
Sentiment: NEGATIVE

Example 4:
Review: اول هلو سان کوییک بعد یه مدل از سن ایچ
Sentiment: NEUTRAL

Example 5:
Review: با بقیه چایی ها هیچ فرقی نداره چه طعم چه رنگ
Sentiment: NEUTRAL

Example 6:
Review: در بسته بندی بهتری اگر عرضه شود خیلی بهتر است
Sentiment: NEUTRAL

Example 7:
Review: خوبه مثل بعضی از مربا ها ابکی نیست
Sentiment: POSITIVE

Example 8:
Review: خوب بود و در باز بودن و طعم خوبی داشت
Sentiment: POSITIVE

Example 9:
Review: عطر و طعمش سلیقه ایه . من که راضی بودم
Sentiment: POSITIVE

Example 10:
Review: خیلی خوب بود اما ظرفش یه کم پر دردسر بود .
Sentiment: OTHER

Example 11:
Review: مزه اش یه جور خاصه تند تند نیس ولی متفاوته
Sentiment: OTHER

Example 12:
Review: با اینکه آب و روغنش زیاد بود اما خوشمزه بود
Sentiment: OTHER

Review: {review}
Sentiment: 
"""

PERSIAN_ZERO = """\
جمله زیر نظر یک شخص است. این جمله به زبان فارسی است. بار یا احساس موجود در این جمله را شناسایی کن.
پاسخ‌ های ممکن کلمات روبرو هستند: POSITIVE, NEUTRAL, NEGATIVE, OTHER.
زمانی که جمله دارای احساس خاصی نیست یا شامل احساسات مختلف است از OTHER استفاده کن

نظر: {review}
احساس:
"""

PERSIAN_ONE = """\
جمله زیر نظر یک شخص است. این جمله به زبان فارسی است. بار یا احساس موجود در این جمله را شناسایی کن.
پاسخ‌ های ممکن کلمات روبرو هستند: POSITIVE, NEUTRAL, NEGATIVE, OTHER.
زمانی که جمله دارای احساس خاصی نیست یا شامل احساسات مختلف است از OTHER استفاده کن

مثال ها:

مثال 1:
نظر: طعم بد . بوی بد . فقط قیمتش خوبه .
احساس: NEGATIVE

مثال 2:
نظر: با بقیه چایی ها هیچ فرقی نداره چه طعم چه رنگ
احساس: NEUTRAL

مثال 3:
نظر: خوب بود و در باز بودن و طعم خوبی داشت
احساس: POSITIVE

مثال 4:
نظر: مزه اش یه جور خاصه تند تند نیس ولی متفاوته
احساس: OTHER

نظر: {review}
احساس:
"""

PERSIAN_THREE = """\
جمله زیر نظر یک شخص است. این جمله به زبان فارسی است. بار یا احساس موجود در این جمله را شناسایی کن.
پاسخ‌ های ممکن کلمات روبرو هستند: POSITIVE, NEUTRAL, NEGATIVE, OTHER.
زمانی که جمله دارای احساس خاصی نیست یا شامل احساسات مختلف است از OTHER استفاده کن

مثال ها:

مثال 1:
نظر: طعم بد . بوی بد . فقط قیمتش خوبه .
احساس: NEGATIVE

مثال 2:
نظر: بعد از ۵ دقیقه مزه اش رو از دست میده
احساس: NEGATIVE

مثال 3:
نظر: طرفش خیلی نازکه تو دست نمیشه نگه داشت
احساس: NEGATIVE

مثال 4:
نظر: اول هلو سان کوییک بعد یه مدل از سن ایچ
احساس: NEUTRAL

مثال 5:
نظر: با بقیه چایی ها هیچ فرقی نداره چه طعم چه رنگ
احساس: NEUTRAL

مثال 6:
نظر: در بسته بندی بهتری اگر عرضه شود خیلی بهتر است
احساس: NEUTRAL

مثال 7:
نظر: خوبه مثل بعضی از مربا ها ابکی نیست
احساس: POSITIVE

مثال 8:
نظر: خوب بود و در باز بودن و طعم خوبی داشت
احساس: POSITIVE

مثال 9:
نظر: عطر و طعمش سلیقه ایه . من که راضی بودم
احساس: POSITIVE

مثال 10:
نظر: خیلی خوب بود اما ظرفش یه کم پر دردسر بود .
احساس: OTHER

مثال 11:
نظر: مزه اش یه جور خاصه تند تند نیس ولی متفاوته
احساس: OTHER

مثال 12:
نظر: با اینکه آب و روغنش زیاد بود اما خوشمزه بود
احساس: OTHER

نظر: {review}
احساس:
"""
