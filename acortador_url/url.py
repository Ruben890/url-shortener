from django.urls import path
from .views import acortadorUrl

urlpatterns = [
    path('', acortadorUrl.as_view(), name='acortadorUrl' )
]