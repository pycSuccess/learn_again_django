from django import forms
from django.core.exceptions import ValidationError
from django.forms import widgets


class MyForm(forms.Form):
    name = forms.CharField(max_length=8, min_length=4, label='姓名', error_messages={"required":"该字段不能为空", "invalid":"格式错误!"})
    tel = forms.IntegerField(label='电话')
    email = forms.EmailField(label='邮箱', error_messages={'invalid':'出错了！'})

# 对一个字段针对性的做限制约束 且是固定用法 clean_属性名 is_valid()能捕获的异常为ValidationError
    def clean_name(self):
        val = self.cleaned_data.get('name')

        if not val.isdigit():
            return val
        else:
            raise ValidationError('用户名不能为纯数字')

# is_valid()执行时才会进行校验：这里有两层校验，第一层校验就是UserForm定义字段的属性，比如类型判断
# 第二层是执行clean_属性名 定义的这些方法。只有通过第一层的校验时，才会进入第二层校验
# 不论第一层还是第二层，通过校验的都放在cleaned_data里面 校验不通过放在errors里面
# 使用全局钩子clean抛出的异常都存在errors的__all__里面


class UserForm(forms.Form):
    # 定义变量，专门给text类型的输入框添加class
    wid = widgets.TextInput(attrs={'class':'form-control'})
    # 定义几种通用的类型返回
    error_hints = { 'required':'该字段不能为空', 'invalid': '格式错误'}
    # 字段定义如下：
    name = forms.CharField(max_length=12, min_length=4, label='姓名', widget=wid, error_messages=error_hints)
    pwd = forms.CharField(label='密码', widget=widgets.PasswordInput(attrs={'class':'form-control'}),
                          error_messages=error_hints)
    r_pwd = forms.CharField(label='确认密码', widget=widgets.PasswordInput(attrs={'class':'form-control'}),
                            error_messages=error_hints)
    age = forms.IntegerField(label='年龄', widget=wid, error_messages=error_hints)
    email = forms.EmailField(label='邮箱', widget=widgets.EmailInput(attrs={'class': 'form-control'}),
                             error_messages=error_hints)
    tel = forms.CharField(label='手机', widget=wid, error_messages=error_hints, max_length=11)

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name.isdigit():
            return name
        else:
            raise ValidationError('用户名不能纯数字')

    def clean_tel(self):
        var = self.cleaned_data.get('tel')
        if len(var) == 11:
            return var
        else:
            raise ValidationError('手机账号必须为11位')

    def clean(self):
        pwd = self.cleaned_data.get('pwd')
        r_pwd = self.cleaned_data.get('r_pwd')
        # 正常逻辑是不用在全局钩子进行判断为空相等的  因为最后才会掉入全局钩子的判断
        if pwd and r_pwd and pwd != r_pwd:
            raise ValidationError('两次密码不一致')
        else:
            # 必须存在该行代码
            return self.cleaned_data
