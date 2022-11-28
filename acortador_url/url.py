from django.urls import path
from .views import  GenericUrlView, url

urlpatterns = [
    path('',  GenericUrlView.as_view(), name='acortadorUrl' ),
    path('url/<str:token>', url, name='url'),
    # path('Qr/<str:url>', Qr.as_view(), name='Qr'),
]