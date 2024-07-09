from django.shortcuts import render
from django.http import response, HttpResponse

def taskList(request):
    return HttpResponse('To do List')
