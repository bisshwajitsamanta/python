from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('<h1> Blog Home Page </h1>')


def about(request):
    return HttpResponse('<h1> Blog About Page </h1>')


def vlog_about(request):
    return HttpResponse('<h1> This is temporary Vlog About Page </h1>')
