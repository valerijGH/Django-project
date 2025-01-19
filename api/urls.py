from django.contrib import admin
from django.urls import path, include
from tutorial.urls import router


urlpatterns = [
    path('', include(router.urls)),
]
