from django import forms


class MyForm(forms.Form):
    name = forms.CharField(max_length=8, min_length=4, label='姓名', error_messages={"required":"该字段不能为空", "invalid":"格式错误!"})
    tel = forms.IntegerField(label='电话')
    email = forms.EmailField(label='邮箱', error_messages={'invalid':'出错了！'})
