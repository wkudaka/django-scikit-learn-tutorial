#language_recognition/views.py
from django.shortcuts import render
from django.views.generic.base import View
#import DetectLanguageForm and detect_language
from language_recognition.forms import DetectLanguageForm
from language_detector import detect_language

class TranslatePhraseView(View):

    template_name = "index.html"

    def get(self, request):

        #create a form object
        form = DetectLanguageForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = DetectLanguageForm(request.POST)
        language = None
        if form.is_valid():
            language = detect_language(form.data['phrase'])

        return render(request, self.template_name, {'form': form, 'language':language})
