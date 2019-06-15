from .models import Question,Choice
from django import forms
class QuestionForm(forms.ModelForm):
    class Meta():
        model = Question
        fields = ('question_text',)
class ChoiceForm(forms.ModelForm):
    class Meta():
        model = Choice
        fields = ('choice_text',)