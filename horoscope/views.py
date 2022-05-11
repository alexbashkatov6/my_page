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

zodiac_bounds = {
                 'aquarius': (21, 1),
                 'pisces': (20, 2),
                 'aries': (21, 3),  # , (20, 4)
                 'taurus': (21, 4),  # , (21, 5)
                 'gemini': (22, 5),  # , (21, 6)
                 'cancer': (22, 6),  # , (22, 7)
                 'leo': (23, 7),  # , (21, 8)
                 'virgo': (22, 8),  # , (23, 9)
                 'libra': (24, 9),  # , (23, 10)
                 'scorpio': (24, 10),  # , (22, 11)
                 'sagittarius': (23, 11),  # , (22, 12)
                 'capricorn': (23, 12), }

month_max_days = {1: 31,
                  2: 29,
                  3: 31,
                  4: 30,
                  5: 31,
                  6: 30,
                  7: 31,
                  8: 31,
                  9: 30,
                  10: 31,
                  11: 30,
                  12: 31
                  }

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


def get_info_by_yyyy(request, sign_zodiac: int):
    return HttpResponse(f"Year {sign_zodiac}")


def get_info_by_float(request, sign_zodiac: float):
    return HttpResponse(f"Float {sign_zodiac}")


def get_info_by_data(request, month: int, day: int):
    # 1. Check month in year range
    if month > 12:
        return HttpResponseNotFound("Введен некорректный номер месяца (>12): {}".format(month))
    # 2. Check day in month days range
    if day > month_max_days[month]:
        return HttpResponseNotFound("Введена некорректная дата: месяц {} день {}".format(month, day))
    # 3. Search algorithm
    prev_sign = 'capricorn'
    for sign in zodiac_bounds:
        start_day, start_month = zodiac_bounds[sign]
        if month == start_month:
            if day >= start_day:
                return HttpResponse(f"Знак зодиака для месяц {month} день {day} = {sign}")
            else:
                return HttpResponse(f"Знак зодиака для месяц {month} день {day} = {prev_sign}")
        prev_sign = sign
    # return HttpResponse(f"Month {month} day {day}")


def get_info(request, sign_zodiac: str):
    description = zodiac_dict.get(sign_zodiac)
    if description:
        return HttpResponse(description)
    return HttpResponseNotFound("Неизвестный знак зодиака {}".format(sign_zodiac))


def get_info_by_number(request, sign_zodiac: int):
    zodiacs = list(zodiac_dict)
    if sign_zodiac > len(zodiacs):
        return HttpResponseNotFound("Неправильный номер знака зодиака {}".format(sign_zodiac))
    name_zodiac = zodiacs[sign_zodiac - 1]
    redirect_url = reverse("horoscope-name", args=(name_zodiac,))
    return HttpResponseRedirect(redirect_url)
