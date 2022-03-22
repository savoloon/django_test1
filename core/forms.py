from django import forms

import core.models


class BookSearch(forms.Form):
    name = forms.CharField(label='Название книги', required=False)
    min_pages = forms.IntegerField(label="Количество страниц", required=False, help_text='Минимальное количество страниц')

    def clean(self):
        raise forms.ValidationError('Ошибка!')

class BookEdit(forms.ModelForm):
    class Meta:
        model = core.models.Book
        fields = '__all__'
