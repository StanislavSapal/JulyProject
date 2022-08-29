from django import forms
from news.models import News
import re
from django.core.exceptions import ValidationError


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        # fields = '__all__'
        fields = ['title', 'content', 'is_published', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'category': forms.Select(attrs={'class': 'form-control'})
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError('Назва не може починатися з цифри')
        return title


class CommentForm(forms.Form):
    comment_text = forms.CharField(label='Ваш коментар', max_length=150, widget=forms.Textarea(
        attrs={"class": "form-control",
               "rows": 3}))

    def clean_comment_text(self):
        comment_text = self.cleaned_data['comment_text']
        if not re.search('[\u0400-\u04FF]', comment_text):
            raise ValidationError('Коментар не може бути написаний латиницею!')
        return comment_text