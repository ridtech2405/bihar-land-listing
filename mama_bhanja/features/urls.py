from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("models/", views.models, name="models"),
    path("projects/", views.projects, name="projects"),
    path("gallery/", views.gallery, name="gallery"),
    path("pricing/", views.pricing, name="pricing"),
    path("career/", views.career, name="career"),
    path("contact/", views.contact, name="contact"),
]