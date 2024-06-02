from django.shortcuts import render
from django.http import HttpResponse



def register(request):
    return render(request,"register/register_page.html")
