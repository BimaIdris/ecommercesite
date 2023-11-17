from django.urls import path
from core.views import index

app_name="coreurls"

urlpatterns=[
    path("",index)
]