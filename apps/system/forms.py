from django import forms

class LoginForm(forms.Form):
    """
    用于用户登录的输入验证
    """
    username = forms.CharField(required=True, error_messages={"required": "请填写用户名"})
    password = forms.CharField(required=True, error_messages={"required": "请填写密码"})