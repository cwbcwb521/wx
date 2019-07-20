from django.shortcuts import render
from django.http import JsonResponse


def ajax_test(request):
    username = request.POST.get("username")
    password = request.POST.get("password")

    datalist = {}

    return JsonResponse(datalist)