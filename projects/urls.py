from django.urls import path
from . import views

urlpatterns = [
    path("", views.starting_page, name="starting-page"), 
    path("projects", views.projects, name="projects-page"), 
    path("projects/<slug:slug>", views.project_detail, name="project-detail-page"),

]