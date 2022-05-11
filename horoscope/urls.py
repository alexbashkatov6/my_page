from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('type/', views.get_type_list),
    path('<int:month>/<int:day>/', views.get_info_by_data),
    path('type/<str:sign_type>/', views.get_signs_for_type_list, name="horoscope-type"),
    path('<int:sign_zodiac>/', views.get_info_by_number),
    path('<str:sign_zodiac>/', views.get_info, name="horoscope-name"),
]
