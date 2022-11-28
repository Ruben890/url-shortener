from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import genericUrl
from .models import acortador_url
import qrcode


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


def url(request, token):
    url = acortador_url.objects.filter(acor_url=token)[0]
    return redirect(url.url)


# class Qr(View):
#     def post(self, request, url, *args, **kwargs):
#         qr = qrcode.QRCode(version=1, box_size=10, border=5)
#         qr.add_data(url)
#         qr.make(fit=True)
#         img = qr.make_image(fill='balck', back_color='white')
#         return render(request, 'QR.html' )
