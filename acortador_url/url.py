from django.urls import path
from .views import  GenericUrlView, url, eliminar

urlpatterns = [
    path('',  GenericUrlView.as_view(), name='acortadorUrl' ),
    path('<str:token>', url, name='url'),
    path('eliminar/<int:id>',eliminar, name='eliminar' )
]