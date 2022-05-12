from django.urls import path, converters, register_converter
from . import views, converters

register_converter(converters.FourDigitYearConverter, "yyyy")
register_converter(converters.MyFloatConverter, "my_float")

urlpatterns = [
    path('', views.index, name="horoscope-index"),
    path('type/', views.get_type_list),
    path('<int:month>/<int:day>/', views.get_info_by_data),
    path('type/<str:sign_type>/', views.get_signs_for_type_list, name="horoscope-type"),
    path('<yyyy:sign_zodiac>/', views.get_info_by_yyyy),
    path('<int:sign_zodiac>/', views.get_info_by_number),
    path('<my_float:sign_zodiac>/', views.get_info_by_float),
    path('<str:sign_zodiac>/', views.get_info, name="horoscope-name"),
]
