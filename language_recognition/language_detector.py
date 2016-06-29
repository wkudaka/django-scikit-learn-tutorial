import os
from sklearn.externals import joblib
from django.core.cache import cache

def detect_language(phrase):

    languages = [
        'ar', #Arabic
        'de', #German
        'en', #English
        'es', #Spanish
        'fr', #French
        'it', #Italian
        'ja', #Japanese
        'nl', #Dutch
        'pl', #Polish
        'pt', #Portuguese (Portugal)
        'ru'  #Russian
    ]

    model_cache_key = 'model_cache'
    model_rel_path = "language_recognition/language_detection_model/model_cache/cache.pkl"

    model = cache.get(model_cache_key)

    if model is None:
        model_path = os.path.realpath(model_rel_path)
        model = joblib.load(model_path)
        #save in django memory cache
        cache.set(model_cache_key, model, None)

    prediction = model.predict([phrase])
    return languages[prediction[0]]
