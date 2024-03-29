from ckeditor.widgets import CKEditorWidget
from django import forms
from .models import DocsPost, DocsCategory


class PostForm(forms.ModelForm):
    body = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = DocsPost
        fields = ('title', 'title_tag', 'author', 'category', 'body', 'snippet', 'header_image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control',
                                             'placeholder': 'имя пользователя',
                                             'value': '',
                                             'id': 'finuser',
                                             'type': 'hidden'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Краткое описание...'}),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = DocsPost
        fields = ('title', 'title_tag', 'category', 'body', 'snippet')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Краткое описание...'}),
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = DocsCategory
        fields = ('name', 'parent')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'parent': forms.Select(attrs={'class': 'form-control'}),
        }
