"""
URL configuration for project_movie project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from movie.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("addg/",Addgenre_view.as_view(),name="addg"),
    path("viewg/",Viewgenre_view.as_view(),name="viewg"),
    path("updateg/<int:pk>",Updategenre_view.as_view(),name="updateg"),
    path("deleteg/<int:pk>",Deletegenre_view.as_view(),name="deleteg"),
    path("addm/",Addmovie_view.as_view(),name="addm"),
    path("viewm/",Viewmovie_view.as_view(),name="viewm"),
    path("updatem/<int:pk>",Updatemovie_view.as_view(),name="updatem"),
    path("deletem/<int:pk>",Deletemovie_view.as_view(),name="deletem"),
    path("filter/<int:pk>",Filter_view.as_view(),name="filter"),
    path("",Homepage_view.as_view(),name="home"),
    path("api/",include("api.urls")),
]
