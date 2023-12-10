from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.template.loader import render_to_string


# Create your views here.


def index(request):
    return render(request, 'main/index.html')
    # t = render_to_string('main/index.html')
    # return HttpResponse(t)



def profile(request):
    return render(request, 'main/profile.html')



def page_not_found(request, exception):
    return HttpResponseNotFound("Такой страницы не существует")

