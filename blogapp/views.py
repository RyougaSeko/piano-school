from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from .forms import ContactForm
from django.contrib import messages
from django.core.mail import EmailMessage


# Create your views here.

from django.views.generic.base import TemplateView

# class IndexView(TemplateView):
#     #index.htmlをレンダリング
#     template_name = 'index.html'

def index_view(request):
    return render(request, 'index.html')

def adlt_view(request):
    return render(request, 'adlt_piano.html')

def child_view(request):
    return render(request, 'child_piano.html')

def teacher_view(request):
    return render(request, 'teacher.html')

def contact_result_view(request):
    return render(request, 'contact_result.html')

class ContactFormView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    # print(form_class)
    success_url = reverse_lazy('blogapp:contact_result')

    # def form_valid(self, form):
    #     form.send_email(form)
    #     return super().form_valid(form)

    def form_valid(self, form):

        '''
        FormViewクラスのform_valid()をオーバーライド

        フォームのバリデーションを通過したデータがPOSTされたときに呼ばれる
        メール送信を行う。

        '''

        #メールのタイトルの書式を設定
        #フォームに登録したデータをフィールド名に指定して取得
        message = form.cleaned_data['message']
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        from_email = 'hoop105ryouga@gmail.com'
        to_list = ['hoop105ryouga@gmail.com']
        title = form.cleaned_data['title']
        subject = "お問い合わせ: {}".format(title)


        #フォームの入力データの書式を指定

        message =  \
            '送信名： {0}\nメールアドレス: {1}\n タイトル:{2}\n メッセージ:\n{3}'\
                .format(name, email, title, message)

        #Emalimessageオブジェクトを生成
        message = EmailMessage(subject, message, from_email, to_list
        )
        #emailメッセージクラスのsend()でメールサーバーからメールを送信
        message.send()

        #送信完了後のメッセージ
        messages.success(
            self.request, 'お問い合わせは正常に送信されました。'
        )

        return super().form_valid(form)


# def contact_view(request):
#     if request.method == 'GET':
#         return render(request, 'contact.html')
#     else:
#         form = ContactForm(request.POST)

#         if form.is_valid():
#             name = form.cleaned_data['name']
#             email = form.cleaned_data['email']
#             title = form.cleaned_data['title']
#             message = form.cleaned_data['message']
#             subject = "お問い合わせ: {}".format(title)

#             from_email = 'hoop105ryouga@gmail.com'
#             to_list = ['hoop105ryouga@gmail.com']

#             #フォームの入力データの書式を指定
#             message =  \
#                 '送信名： {0}\nメールアドレス: {1}\n タイトル:{2}\n メッセージ:\n{3}'\
#                     .format(name, email, title, message)

#             #Emalimessageオブジェクトを生成
#             message = EmailMessage(subject=subject,
#             body=message,
#             from_email=from_email,
#             to=to_list,
#             )
#             #emailメッセージクラスのsend()でメールサーバーからメールを送信
#             message.send()

#             #送信完了後のメッセージ
#             message.success(
#                 request, 'お問い合わせは正常に送信されました。'
#             )
#             # return render(request, 'index.html')
#             print("OK")

#         else:
#             return render(request, 'index.html')


# class ContactResultView(TemplateView):
#     template_name = 'contact_result.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['success'] = "お問い合わせは正常に送信されました。"

#argsは引数全て、*argsは引数を受け取る方法の1つ。
#タプルで引数を受け取る。
#引数を複数渡せる
#**kwargsは、辞書で引数を受け取る。

# def hello(*args):
#     print(args)
    
# hello("hiroki", "saito")  # ('hiroki', 'saito') と表示されます