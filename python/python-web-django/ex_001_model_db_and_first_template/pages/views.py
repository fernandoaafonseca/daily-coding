from django.shortcuts import render
from django.http import HttpResponse


def home_view(request):
    return render(request, 'home.html', {})

def about_admin_view(request):
    return render(request, 'about_admin.html', {})

def about_templates_view(request):
    return render(request, 'about_templates.html', {})