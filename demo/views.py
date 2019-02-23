from django.shortcuts import render


# Create your views here...
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

# Create your views here.



@csrf_exempt
def index(request):
    if request.method == 'POST':
        session_id = request.POST.get('sessionId')
        service_code = request.POST.get('serviceCode')
        phone_number = request.POST.get('phoneNumber')
        text = request.POST.get('text')

        response = ""

        if text == "":
            response = "CON Welcome To Smart Tickets \n"
            # response .= "1. Movie Ticket \n"
            response += "1. Movie Ticket"
            # response .= "1. Events Ticket \n"
            response += "2. Events Ticket"

        elif text == "1":
            response = "CON Choose A Location \n"
            # response .= "1. Lagos \n"
            response += "1. Lagos"
            # response .= "2. PH \n"
            response += "2. PH"
            # response .= "3. Abuja \n"
            response += "3. Abuja"

            response = "END My Phone number is {0}".format(phone_number)

        elif text == "2":
            response = "END Comming Soon "

        return HttpResponse(response)
