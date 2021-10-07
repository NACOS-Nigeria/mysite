from .models import Client
from .models import Client_road
from .models import Client_contact
from django.forms import ModelForm, TextInput, Textarea


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ["Person", "Number", "text"]

        widgets = {
            "Person": TextInput(attrs={
                "class": "contacting-box",
                "placeholder": "Имя"
            }),
            "Number": TextInput(attrs={
                "class": "contacting-box",
                "placeholder": "Номер телефона"
            }),
            "text": TextInput(attrs={
                "class": "contacting-box",
                "placeholder": "Отзыв"
            })

        }


class Client_roadForm(ModelForm):
    class Meta:
        model = Client_road
        fields = ["date", "point_A", "point_B", "thing", "telephone", "name", "time_to_call"]

        widgets = {

            "date": TextInput(attrs={
                "class": "quote-box",
                "placeholder": "Дата перевозки*"
            }),
            "point_A": TextInput(attrs={
                "class": "quote-box",
                "placeholder": "Откуда перевозим?*"
            }),
            "point_B": TextInput(attrs={
                "class": "quote-box",
                "placeholder": "Куда везём?*"
            }),
            "thing": TextInput(attrs={
                "class": "quote-box",
                "placeholder": "Что перевозим?*"
            }),
            "telephone": TextInput(attrs={
                "class": "quote-box",
                "placeholder": "Контактный телефон*"
            }),
            "name": TextInput(attrs={
                "class": "quote-box",
                "placeholder": "Имя клиента*"
            }),
            "time_to_call": TextInput(attrs={
                "class": "quote-box",
                "placeholder": "Когда перезвонить?*"
            })

        }


class Client_contactForm(ModelForm):
    class Meta:
        model = Client_contact
        fields = ["name", "email", "text"]

        widgets = {

            "name": TextInput(attrs={
                "class": "contact-box",
                "placeholder": "Ф.И.O.*"
            }),
            "email": TextInput(attrs={
                "class": "contact-box",
                "placeholder": "Email*"
            }),
            "text": TextInput(attrs={
                "class": "contact-box",
                "placeholder": "Текст сообщения*"
            })
        }
