from django import forms
from .models import BigIdeaRubric, CoreComp, Evidence, Student

class CESForm(forms.Form):
    subject = forms.ModelChoiceField(queryset=BigIdeaRubric.objects.values('courseName'))
    icanstatement = forms.ModelChoiceField(queryset=CoreComp.objects.values('iCan'))