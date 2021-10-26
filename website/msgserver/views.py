from django.shortcuts import render
from msgserver.models import Message
from django.http import HttpResponse
# Create your views here.

def get_msg(request, key):
    message = Message.objects.filter(key = key)
    if (len(message) > 0):
        #return HttpResponse( "Message is: " + str(Message.objects.get(key=key)))
        #return HttpResponse(Message.objects.get(key=key))
        return HttpResponse(message)
    else:
        return HttpResponse("No message")
    



