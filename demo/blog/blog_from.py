# coding:utf-8

from django import forms


class UserInfo(forms.Form):
    username = forms.CharField(max_length=32)
    password = forms.CharField(max_length=32)
