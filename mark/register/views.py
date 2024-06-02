from django.shortcuts import render, redirect

from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm



def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request,data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request,user) #
                return redirect("index")
    else:
        form = AuthenticationForm()
    return render(request,"register/login_page.html", {"form":form})

def log_out(request):
    logout(request)
    return redirect("index")


def register(request):
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request,"register/register_page.html", {"form":form})
