from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_protect
from django.template import loader
from .models import *

@csrf_protect
def index(request):
    template = loader.get_template('cv_app/index.html')
    return HttpResponse(template.render({},request))

def menu(request):
    if request.method == "POST":
        name = request.POST.get('name')
        template = loader.get_template('cv_app/menu.html')
        return HttpResponse(template.render({"name": name},request))
    else:
        return HttpResponseBadRequest("You should provide your name to continue")

def complete_cv(request):
    template = loader.get_template('cv_app/complete_cv.html')
    return HttpResponse(template.render({},request))

def personal_info(request):
    name = Person.objects.get(id="1007286825").name
    age = Person.objects.get(id="1007286825").age
    birth_date = Person.objects.get(id="1007286825").birth_date
    context = {"name": name, "age": age, "birth_date": birth_date}
    template = loader.get_template('cv_app/personal_information.html')
    return HttpResponse(template.render(context, request))

def studies(request):
    template = loader.get_template('cv_app/studies.html')
    return HttpResponse(template.render({}, request))

def work_experience(request):
    template = loader.get_template('cv_app/work_experience.html')
    return HttpResponse(template.render({}, request))

def additional_info(request):
    template = loader.get_template('cv_app/additional_info.html')
    return HttpResponse(template.render({}, request))
