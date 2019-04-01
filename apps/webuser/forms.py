# -*- coding: utf-8 -*-

from django import forms


class LoginForm(forms.Form):
    sign_data = forms.CharField()
    to_sign = forms.CharField(max_length=64, required=False)
    sign = forms.CharField(max_length=1000)
    public_key = forms.CharField(max_length=100)
    name = forms.CharField(max_length=100)
    source = forms.IntegerField(min_value=1, max_value=2)



