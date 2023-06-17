from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.views.generic import View
from django.contrib.auth.admin import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.views.generic.edit import FormView
from django.contrib.auth import login

from .models import Acortador_url
from .forms import genericUrl, LoginForm, UserRegister


###*# Vista para la página principal
class GenericUrlView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html', {'form': genericUrl,
                                              'url': Acortador_url.objects.all().order_by('-acor_url')})
    def post(self, request, *args, **kwargs):
        user = get_object_or_404(User, pk=request.user.pk)
        form = genericUrl(request.POST)
        if form.is_valid():
            url = form.save(commit=False)
            url.profiles = user
            url.save()
            return redirect('url_shorcuter')
        
###* redireccionar a la url 
def url(request, token):
    url_obj = Acortador_url.objects.filter(acor_url=token).first()

    if url_obj:
        return redirect(url_obj.url)
    else:
        return HttpResponse("URL no encontrada")


###* eliminar url
def eliminar(request, id):
    url = Acortador_url.objects.get(id=id)
    url.delete()
    return redirect('url_shorcuter')



###? Auth AUTHENTICATION
###* Vista para el inicio de sesión
class Login(LoginView):
    template_name = 'login.html'
    fields = '__all__'
    authentication_form = LoginForm
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('url_shorcuter')

###*Vista para el registro de usuario
class Register(FormView):
    fields = '__all__'
    template_name = 'register.html'
    form_class = UserRegister
    redirect_authenticated_user = True
    success_url = reverse_lazy('url_shorcuter')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(Register, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return reverse_lazy('url_shorcuter')
        return super(Register, self).get(*args, **kwargs)