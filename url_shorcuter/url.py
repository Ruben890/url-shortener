from django.urls  import path
from .views import GenericUrlView, Login, Register,url, eliminar
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('',GenericUrlView.as_view(), name='url_shorcuter'),
    path('token/<str:token>', url, name='url'),
    path('eliminar/<int:id>',eliminar, name='eliminar'),
    
    ###? Auth AUTHENTICATION
    path('login', Login.as_view(), name="login"),
    path('register', Register.as_view(), name="register"),
    path('Logaut', LogoutView.as_view(next_page='login'), name='logaut'),
    
]