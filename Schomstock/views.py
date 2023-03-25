from django.shortcuts import render
from django.http.response import JsonResponse


def Home(request):
    return render(request, 'Home.html')
