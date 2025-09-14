from django import forms
from django.core.exceptions import ValidationError

from .models import Product

ban_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар', ]


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'category', 'price', 'image', ]

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Название товара',
        })

        self.fields['description'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Описание товара',
            'style': 'height: 80px;',
        })

        self.fields['category'].widget.attrs.update({
            'class': 'form-control',
        })

        self.fields['price'].widget.attrs.update({
            'class': 'form-control',
        })

        self.fields['image'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Изображение товара',
        })

    def clean_name(self):
        name = self.cleaned_data.get('name')
        for word in ban_words:
            if word.lower() in name.lower():
                raise ValidationError(f'Нельзя использовать слово {word} в названии товара')
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description')
        for word in ban_words:
            if word.lower() in description.lower():
                raise ValidationError(f'Нельзя использовать слово {word} в описании товара')
        return description

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price < 0:
            raise ValidationError('Цена не может быть отрицательной')

    def clean_image(self):
        if self.cleaned_data.get('image'):
            image = self.cleaned_data.get('image')
            if image.size > 5000000:
                raise ValidationError('Размер изображения не должен превышать 5 МБ')
            if image.content_type not in ['image/jpeg', 'image/png']:
                raise ValidationError('Изображение должно быть в формате JPEG или PNG')
            return image
        return None
