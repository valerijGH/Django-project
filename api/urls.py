from django.contrib import admin
from django.urls import path, include
from tutorial.urls import router

from . import views
from .views import ProfessionViewSet, GeneralStatisticsViewSet

router.register(r'professions', ProfessionViewSet)
router.register(r'statistics', GeneralStatisticsViewSet)

urlpatterns = [
    path("notes/", views.NoteListView.as_view(), name="note-list"),
    path("notes/delete/<int:pk>", views.NoteDeleteView.as_view(), name="note-delete"),
    path('', include(router.urls)),
]
