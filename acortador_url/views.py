from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import genericUrl
from .models import acortador_url


class GenericUrlView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html', {'form': genericUrl,
                                              'url': acortador_url.objects.all().order_by('-acor_url')})

    def post(self, request, *args, **kwargs):
        form = genericUrl(request.POST)

        if form.is_valid():
            new_url = form.save(commit=False)
            new_url.save()
        return redirect('acortadorUrl')

# * redirigir url


def url(request, token):
    url = acortador_url.objects.filter(acor_url=token).first()
    return redirect(url.url)

# * eliminar url


def eliminar(request, id):
    url = acortador_url.objects.get(id=id)
    url.delete()
    return redirect('acortadorUrl')
