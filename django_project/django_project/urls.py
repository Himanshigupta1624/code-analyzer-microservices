"""
URL configuration for django_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from home.views import start_task,task_status_view
from django.http import HttpResponse

def test_view(request):
    return HttpResponse("Django routing works!")

urlpatterns = [
    path('test/', test_view),
    path('start_task/',start_task),
    path('task_status_view/<str:task_id>/',task_status_view),
    path('admin/', admin.site.urls),
]
