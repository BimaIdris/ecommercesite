from django.urls import path
from userauths import views

app_name='userauths'

urlpatterns=[
    path("register/",views.register_view,name="register"),
    path("sign-in/",views.login_view,name="sign-in"),
]