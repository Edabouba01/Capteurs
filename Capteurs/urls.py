from appcapteur.views import temperaturApi,pressionApi,MesurApi
from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('temperatur/', temperaturApi.as_view()),
     path('humidite/', MesurApi.as_view()),
     path('pression/', pressionApi.as_view()),
      
]
