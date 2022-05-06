from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
import math
from django.urls import reverse


# Create your views here.
def get_rectangle_area(request, width, height):
    return HttpResponse("Площадь прямоугольника размером {}х{} равна {}".format(width, height, width*height))


def get_square_area(request, width):
    return HttpResponse("Площадь квадрата размером {}х{} равна {}".format(width, width, width*width))


def get_circle_area(request, radius):
    return HttpResponse("Площадь круга радиусом {} равна {}".format(radius, math.pi*radius*radius))


def get_rectangle_area_redir(request, width, height):
    addr = reverse("rectangle", args=(width, height))
    return HttpResponseRedirect(addr)
    # return HttpResponseRedirect("/geometry/rectangle/{}/{}/".format(width, height))


def get_square_area_redir(request, width):
    addr = reverse("square", args=(width,))
    return HttpResponseRedirect(addr)
    # return HttpResponseRedirect("/geometry/square/{}".format(width))


def get_circle_area_redir(request, radius):
    addr = reverse("circle", args=(radius,))
    return HttpResponseRedirect(addr)
    # return HttpResponseRedirect("/geometry/circle/{}".format(radius))


