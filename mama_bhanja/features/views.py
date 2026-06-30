from django.shortcuts import render

def home(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def models(request):
    return render(request, "models.html")

def projects(request):
    return render(request, "projects.html")

def gallery(request):
    return render(request, "gallery.html")

def pricing(request):
    return render(request, "pricing.html")

def career(request):
    return render(request, "career.html")

def contact(request):
    return render(request, "contact.html")