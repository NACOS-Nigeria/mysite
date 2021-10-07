from .models import AddCallForm
from django.forms import ModelForm, TextInput


class AddCallFormForm(ModelForm):
    class Meta:
        model = AddCallForm
        fields = ["name", "fone"]

        widgets = {
            "name": TextInput(attrs={
                "class": "bkackeogun",
                "placeholder": "ИМЯ"
            }),
            "fone": TextInput(attrs={
                "class": "bkackeogun",
                "placeholder": "Телефон"
            })

        }
