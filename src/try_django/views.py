from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template

def home_page(request):
    return render(request, "home.html", {"title": "Home"})

def about_page(request):
    return render(request, "about.html", {"title": "About Us"})


def contact_page(request):
    return render(request, "contact.html", {"title": "Contact Us"})

def example_page(request):
    context = {"title": "Example"}
    template_name = "example.html"
    template_obj = get_template(template_name)
    return HttpResponse(template_obj.render(context))