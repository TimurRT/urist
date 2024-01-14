from django.shortcuts import render, redirect
from .forms import UserInfoForm
from django.core.mail import send_mail
from django.conf import settings
import re


def home(request):
    company_name = "Юридический путиводитель"
    return render(request, 'index.html', {'company_name': company_name})


def uslugi(request):
    return render(request, 'uslugi.html')


def prices(request):
    company_name = "Цены"
    return render(request, 'price.html', {'company_name': company_name})

def onas(request):
    return render(request, 'onas.html')


def is_russian_phone_number(phone):
    # Regular expression for Russian phone numbers
    russian_phone_pattern = re.compile(r'^(\+7|8) \(\d{3}\) \d{3}-\d{2}-\d{2}$')
    return bool(re.match(russian_phone_pattern, phone))


def user_data_form(request):
    if request.method == 'POST':
        form = UserInfoForm(request.POST)
        if form.is_valid():
            if not is_russian_phone_number(form.cleaned_data["phone"]):
                form.add_error('phone', 'Пожалуйста, введите правильный российский номер телефона.')
            else:
                form.save()
            send_mail(
                'Новые данные пользователя',
                f'Имя: {form.cleaned_data["name"]}\nНомер телефона: {form.cleaned_data["phone"]}\nEmail: {form.cleaned_data["email"]}',
                settings.DEFAULT_FROM_EMAIL,
                ['consulturist2024@yandex.ru'],
                fail_silently=False,
            )

            return redirect('index.html')
    else:
        form = UserInfoForm()

    return render(request, 'user_info_form.html', {'form': form})
