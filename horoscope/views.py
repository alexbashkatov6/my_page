from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def leo(request):
    return HttpResponse("знак зодиака лев")


def scorpion(request):
    return HttpResponse("знак зодиака скорпион")
