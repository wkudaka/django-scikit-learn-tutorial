from django import forms

class DetectLanguageForm(forms.Form):
    phrase = forms.CharField(
                            required=True,
                            widget=forms.Textarea,
                            error_messages={'required': 'Message is required'}
                            )


    phrase.widget.attrs['class'] = 'form-control'
