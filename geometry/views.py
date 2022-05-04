from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
import math


# Create your views here.
def get_rectangle_area(request, width, height):
    return HttpResponse("Площадь прямоугольника размером {}х{} равна {}".format(width, height, width*height))


def get_square_area(request, width):
    return HttpResponse("Площадь квадрата размером {}х{} равна {}".format(width, width, width*width))


def get_circle_area(request, radius):
    return HttpResponse("Площадь круга радиусом {} равна {}".format(radius, math.pi*radius*radius))


def get_rectangle_area_redir(request, width, height):
    return HttpResponseRedirect("/geometry/rectangle/{}/{}/".format(width, height))


def get_square_area_redir(request, width):
    return HttpResponseRedirect("/geometry/square/{}".format(width))


def get_circle_area_redir(request, radius):
    return HttpResponseRedirect("/geometry/circle/{}".format(radius))


