from django.shortcuts import render
from .models import home 
from users.models import Contact
from django.http import JsonResponse
import json
# Create your views here.



def homeview(request):
    context = Contact.objects.all()
    template_name = 'index.html'
    return render(request,template_name,{'context':context})

def contactview(request):
    context = Contact.objects.all()
    print(context)
    template_name = 'index.html'
    return JsonResponse({'context':'bar'})

