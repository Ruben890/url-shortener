from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.views.generic.edit import FormView
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from .models import Acortador_url
from .forms import GenericUrlForm, LoginForm, UserRegister


# *# Vista para la página principal
class GenericUrlView(LoginRequiredMixin, View):
    def get(self, request):
        generic_url_form = GenericUrlForm()
        urls = Acortador_url.objects.all().order_by('-acor_url')
        return render(request, 'index.html', {'form': generic_url_form, 'urls': urls})

    def post(self, request):
        user = request.user
        form = GenericUrlForm(request.POST)
        if form.is_valid():
            url = form.save(commit=False)
            url.profiles = user
            url.save()
            return redirect('/')
        return render(request, 'index.html', {'form': form, 'urls': Acortador_url.objects.all().order_by('-id')})

# * redireccionar a la url


def redireccionar_url(request, acor_url):
    acortador = get_object_or_404(Acortador_url, acor_url=acor_url)
    return HttpResponseRedirect(acortador.url)


# * eliminar url
def eliminar(request, id):
    url = Acortador_url.objects.get(id=id)
    url.delete()
    return redirect('home')


# ? Auth AUTHENTICATION
# * Vista para el inicio de sesión
class Login(LoginView):
    template_name = 'login.html'
    fields = '__all__'
    authentication_form = LoginForm
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')

# *Vista para el registro de usuario


class Register(FormView):
    fields = '__all__'
    template_name = 'register.html'
    form_class = UserRegister
    redirect_authenticated_user = True
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(Register, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return reverse_lazy('home')
        return super(Register, self).get(*args, **kwargs)
