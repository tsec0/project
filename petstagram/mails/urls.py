from django.urls import path

from mails.views import delete_mail, preview_mail, create_mail, mail_inbox, is_read

urlpatterns = [
    path('inbox/', mail_inbox, name='mail inbox'),
    path('isread/<int:pk>', is_read, name='read mail'),
    path('edit/<int:pk>/', preview_mail, name='edit mail'),
    path('delete/<int:pk>/', delete_mail, name='delete mail'),
    # path('create/', create_mail, name='create mail'),
    path('create/<int:pk>', create_mail, name='send to pet user'),
    # path('resend/<int:pk>', create_mail, name='resend mail')
]
