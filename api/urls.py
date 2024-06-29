from django.urls import path
from api.views import *
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
routers=DefaultRouter()

router.register("genre",Genre_viewset,basename="genre")
routers.register("movie",Movie_viewset,basename="movie")





urlpatterns=[

]+router.urls+routers.urls