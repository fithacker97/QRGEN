from django.shortcuts import render
from .forms import QRCodeForm 
import qrcode

def generate_qr(request):
    if request.method == 'POST':
        form = QRCodeForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            url = form.cleaned_data['url']
            qr = qrcode.make(url)
            filename = name.replace(" ", "_") + '_qr.png'
            from django.conf import settings
            import os
            filepath = os.path.join(settings.MEDIA_ROOT, filename)
            qr.save(filepath)

            qr_code_url = os.path.join(settings.MEDIA_URL, filename)
            context = {
                'name': name,
                'qr_code_url': qr_code_url
            }
            return render(request, 'result.html', context )
    else:
        form = QRCodeForm()
        context = {'form': form}
        return render(request, 'generate_qr.html', context)


