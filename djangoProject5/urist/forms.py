# myapp/forms.py
from django import forms
from .models import UserInfo
import re


def is_russian_phone_number(phone):
    # Регулярное выражение для российских номеров телефонов
    russian_phone_pattern = re.compile(r'^(\+7|8)[\s\(]*\d{3}[\s\)]*\d{3}[\s-]*\d{2}[\s-]*\d{2}$')
    return bool(re.match(russian_phone_pattern, phone))


class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ['name', 'phone', 'email']

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if not is_russian_phone_number(phone):
            raise forms.ValidationError('Пожалуйста, введите правильный российский номер телефона.')
        return phone
