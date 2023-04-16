from django.shortcuts import render


def index(request):
    return render(request, 'index.html', {})


def bmi(request):  # New function
    return render(request, 'bmi.html', {})
