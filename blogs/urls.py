from django.urls import path
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1> Hello I Ohm </h1>")

urlpatterns=[
    path('',index)
]