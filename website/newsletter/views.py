from django.shortcuts import render
from .forms import NewsletterForm

from django.core.mail import send_mail


# Create your views here.

def suscribe(request):

    sent = False

    form = NewsletterForm()

    if request.method == 'POST':
        form = NewsletterForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            to = data.get('email')
            subject = "Newsletter Subsription"
            message = 'Thank you for suscribing with us!'

            send_mail(subject, message, 'hitesh53gharat@gmail.com', [to,])

            sent = True

    context = {
        'form' : form,
        'sent' : sent
    }
    
    return render(request,'newsletter/newsletter.html',context)
