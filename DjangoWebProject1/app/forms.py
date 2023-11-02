"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))

class AnketaForm(forms.Form):
    name = forms.CharField(label='���� ���', min_length=2, max_length=100)
    city = forms.CharField(label='��� �����', min_length=2, max_length=100)
    job = forms.CharField(label='��� ��� �������', min_length=2, max_length=100)
    gender = forms.ChoiceField(label='��� ���', choices=[('1', '�������'),('2', '�������')],
                               widget = forms.RadioSelect,initial=1)
    internet = forms.ChoiceField(label='�� ����������� ����������', choices=(('1', '������ ����'),('2', '��������� ��� � ����'), ('3','��������� ��� � ������'), ('4','��������� ��� � �����')),initial=1)
    notice = forms.BooleanField(label='�������� ������� ����� �� e-mail?', required=False)
    email = forms.EmailField(label='��� e-mail', min_length=7)
    message = forms.CharField( label='������� � ����', widget=forms.Textarea(attrs={'rows':12, 'cols':20}))        
    
