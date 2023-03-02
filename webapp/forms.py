import ordering as ordering
from django import forms
from django.core.exceptions import ValidationError
from django.forms import widgets

from webapp.models import Issue


class IssueForm(forms.ModelForm):

    class Meta:
        model = Issue
        fields = ("summary", "description", 'type', 'status')

        labels = {
            "summary": 'Заголовок',
            "description": 'Описание',
            "type": 'Тип',
            "status": 'Статус'
        }



    def clean_summary(self):
        summary = self.cleaned_data.get("summary")
        if len(summary) < 2:
            raise ValidationError("Summary must be longer than 2 characters")
        return summary

