from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Gracias por contactarnos! Tu mensaje ha sido enviado correctamente.')
            return redirect('contract:contact')
    else:
        form = ContactForm()
    
    return render(request, 'contract/contact.html', {
        'form': form,
        'title': 'Contacto'
    })
