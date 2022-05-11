from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.


# def leo(request):
#     return HttpResponse("знак зодиака лев!")
#
#
# def scorpion(request):
#     return HttpResponse("знак зодиака скорпион")

zodiac_dict = {'aries': 'Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).',
               'taurus': 'Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).',
               'gemini': 'Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).',
               'cancer': 'Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).',
               'leo': 'Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).',
               'virgo': 'Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).',
               'libra': 'Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).',
               'scorpio': 'Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).',
               'sagittarius': 'Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).',
               'capricorn': 'Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).',
               'aquarius': 'Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).',
               'pisces': 'Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).', }

type_to_sign_list = {
    'fire': ['aries', 'leo', 'sagittarius'],
    'earth': ['taurus', 'virgo', 'capricorn'],
    'air': ['gemini', 'libra', 'aquarius'],
    'water': ['cancer', 'scorpio', 'pisces']
}


def index(request):
    zodiacs = list(zodiac_dict)
    li_elements = ""
    for sign in zodiacs:
        redirect_path = reverse("horoscope-name", args=(sign,))
        li_elements += f"<li> <a href='{redirect_path}'> {sign.title()} </a> </li>"
    response = f"""
    <ul>
        {li_elements}
    </ul>
    """
    return HttpResponse(response)


def get_type_list(request):  # , sign_zodiac: str
    zodiac_types = list(type_to_sign_list)
    li_elements = ""
    for zodiac_type in zodiac_types:
        redirect_path = reverse("horoscope-type", args=(zodiac_type,))
        li_elements += f"<li> <a href='{redirect_path}'> {zodiac_type.title()} </a> </li>"
    response = f"""
    <ul>
        {li_elements}
    </ul>
    """
    return HttpResponse(response)


def get_signs_for_type_list(request, sign_type: str):
    sign_list = type_to_sign_list.get(sign_type)
    if sign_list:
        li_elements = ""
        for sign in sign_list:
            redirect_path = reverse("horoscope-name", args=(sign,))
            li_elements += f"<li> <a href='{redirect_path}'> {sign.title()} </a> </li>"
        response = f"""
        <ul>
            {li_elements}
        </ul>
        """
        return HttpResponse(response)
    return HttpResponseNotFound("Неизвестный тип знаков зодиака {}".format(sign_type))


def get_info(request, sign_zodiac: str):
    description = zodiac_dict.get(sign_zodiac)
    if description:
        return HttpResponse(description)
    return HttpResponseNotFound("Неизвестный знак зодиака {}".format(sign_zodiac))


def get_info_by_number(request, sign_zodiac: int):
    zodiacs = list(zodiac_dict)
    if sign_zodiac > len(zodiacs):
        return HttpResponseNotFound("Неправильный номер знака зодиака {}".format(sign_zodiac))
    name_zodiac = zodiacs[sign_zodiac-1]
    redirect_url = reverse("horoscope-name", args=(name_zodiac,))
    return HttpResponseRedirect(redirect_url)
