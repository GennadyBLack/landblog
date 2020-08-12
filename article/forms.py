from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):

    title = forms.CharField(label='Название поста', max_length=500, required=True)
    title.widget.attrs.update({'class': 'article--title'})
    body = forms.CharField(label='Текст поста', max_length=500, required=True)
    body.widget.attrs.update({'class': 'article--body'})
    description = forms.CharField(label='Описание поста', max_length=500, required=True)
    description.widget.attrs.update({'class': 'article--description'})


    class Meta:
        model = Article
        fields = ['title', 'body','description','poster']