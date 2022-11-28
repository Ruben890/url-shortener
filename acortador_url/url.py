from django.urls import path
from .views import  GenericUrlView, url

urlpatterns = [
    path('',  GenericUrlView.as_view(), name='acortadorUrl' ),
    path('<str:token>', url, name='url')
]