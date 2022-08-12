from django.urls import path
from . import views
from .views import ContactFormView

#URLConfのURLパターンを逆引きできるようにアプリ名を登録
app_name = 'blogapp'

# urlpatterns = [
#     path('', views.IndexView.as_view(), name = 'index'),
# ]
urlpatterns = [
    path('', views.index_view, name='index'),
    path('contact/', ContactFormView.as_view(), name='contact'),
    path('adlt_piano/', views.adlt_view, name='adlt_piano'),
    path('child_piano/', views.child_view, name='child_piano'),
    path('teacher/', views.teacher_view, name='teacher'),
    path('contact_result/', views.contact_result_view, name='contact_result'),



    # path('contact/', views.contact_view, name='contact'),
    # path('contact/', ContactFormView.as_view(), name='contact_form'),
    # path('contact/result/', ContactResultView.as_view(), name='contact_result'),

]