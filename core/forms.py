from django import forms

import core.models


class BookSearch(forms.Form):
    name = forms.CharField(label='Название', required=False)
    pages = forms.IntegerField(label='Кол-во страниц', required=False, help_text='Минимальное количество страниц')
    author = forms.ModelChoiceField(label='Автор книги', queryset=core.models.Author.objects.all(), to_field_name='name')

    def clean(self):
        raise forms.ValidationError('Ошибка!')


class BookEdit(forms.ModelForm):
    class Meta:
        model = core.models.Book
        fields = '__all__'