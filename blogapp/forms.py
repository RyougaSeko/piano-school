from email.message import EmailMessage
# from turtle import title
from django import forms
from django.conf import settings
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse

#モデルクラスのようなもの
class ContactForm(forms.Form):
    #field(メンバ、プロパティ)を定義

    # title = forms.CharField(
    #     label = '',
    #     widget=forms.TextInput(attrs={
    #         'class': 'form-control',
    #         'placeholder': "件名",
    #     }), 
    # )
    
    name = forms.CharField(
        label='',
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': "お名前",
        }), 
    )

    #emailというメンバ（フィールド、プロパティ）を定義
    email = forms.EmailField(
        label='',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': "メールアドレス",
        }),
    )

    message = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': "お問い合わせ内容",
        }),
    )

    def __init__(self, *args, **kwargs):
        '''
        ContactFormのコントラクタ
        フィールドの初期化
        '''

        super().__init__(*args, **kwargs)
        # self.fields['name'].widget.attrs['placeholder'] = \
        #     'お名前を入力してください'

 
        # from_email = '{name} <{email}>'.format(name=name, email=email)
        # recipient_list = [settings.EMAIL_HOST_USER]  # 受信者リスト
        # try:
        #     send_mail(subject, message, from_email, recipient_list)
        # except BadHeaderError:
        #     return HttpResponse("無効なヘッダが検出されました。")