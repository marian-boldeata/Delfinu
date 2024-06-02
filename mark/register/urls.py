from . import views
from django.urls import path




urlpatterns =[
    path("login/", views.login_view, name="login"),
    path('logout', views.log_out, name="logout"),
    path("register/", views.register, name = "register")

]