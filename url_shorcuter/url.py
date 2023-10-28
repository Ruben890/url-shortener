from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', GenericUrlView.as_view(), name='home'),
    path('<str:acor_url>/', redireccionar_url, name='redirect_url'),
    path('eliminar/<int:id>', eliminar, name='eliminar'),

    # ? Auth AUTHENTICATION
    path('login', Login.as_view(), name="login"),
    path('register', Register.as_view(), name="register"),
    path('logout', LogoutView.as_view(next_page='login'), name='logout'),

]
