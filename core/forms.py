from django import forms

import core.models


class BookSearch(forms.Form):
    name = forms.CharField(label='Название', required=False)
    author = forms.ModelChoiceField(label='Автор книги', queryset=core.models.Author.objects.all(), required=False)
    genre = forms.ModelChoiceField(label='Жанр книги', queryset=core.models.Genre.objects.all(), required=False)


class BookEdit(forms.ModelForm):
    class Meta:
        model = core.models.Book
        fields = '__all__'
