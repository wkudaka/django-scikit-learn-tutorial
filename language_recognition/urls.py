#language_recognition/urls.py
from django.conf.urls import url

from views import TranslatePhraseView

urlpatterns = [
    url(r'^', TranslatePhraseView.as_view(), name='index'),
]
