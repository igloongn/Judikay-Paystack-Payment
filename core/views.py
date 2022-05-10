from django.shortcuts import render
from django.conf import settings
import secrets


# Create your views here.


def initiate_payment(request):
    p = {}

    if request.method == 'POST':
        # will get the Email if the email exist else it will be saved as None
        email = request.POST.get('email')
        # will save the amount if the amount exist else it will return as error
        amount = request.POST['amount']
        
        ref = secrets.token_urlsafe(20)
        # Send the Gotten Details to the Posted HTML Page
        p['email'] = email
        p['amount'] = amount
        p['ref'] = ref
        p['paystackAmount'] = int(amount) * 100
        p['publicKey'] = settings.PUBLIC_KEY
        return render(request, 'payment/make_payment.html', p)

    return render(request, 'payment/initiate_payment.html', p)
