from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm


class CustomerUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields
        widgets = {

        }
class form(forms.ModelForm):
    class Meta:
        model=product
        fields=[
            'name',
            'image',
            'price',
            'quantity',
            'addedby'

        ]


class checkout_form(forms.ModelForm):
    class Meta:
        model=checkout
        fields=[
            'firstname',
            'lastname',
            'country',
            'address',
            'city',
            'state',
            'pincode',
            'phone',
            'email',

        ]

class product_regform(forms.ModelForm):
    class Meta:
        model=product
        fields=[
            'name',
            'image',
            'price',
            'quantity',

        ]



