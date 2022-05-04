from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

# Create your views here.

week_days_dict = {"monday": "понедельник",
                  "tuesday": "вторник",
                  "wednesday": "среда",
                  "thursday": "четверг",
                  "friday": "пятница",
                  "saturday": "суббота",
                  "sunday": "воскресенье",
                  }


def get_info(request, week_day):
    russian_day = week_days_dict.get(week_day)
    if russian_day:
        return HttpResponse(russian_day)
    else:
        return HttpResponseNotFound("Неизвестный день недели {}".format(week_day))


def get_info_int(request, week_day):
    if week_day in range(1, 8):
        return HttpResponseRedirect("/todo_week/{}".format(list(week_days_dict)[week_day-1]))
    else:
        return HttpResponseNotFound("Неверный номер дня {}".format(week_day))
