from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name="home"),
    path('sign-up/', views.sign_up, name="sign_up"),
    path("logout/", views.logOut, name ="logout"), 
    path("create-project/", views.create_project, name ="create_post"), 
    path('project/<int:pk>/update', views.update_project, name="update_project"), 
    path('celebration-wall', views.celebration_wall, name='celebration_wall')
]