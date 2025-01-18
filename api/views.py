from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from api.serializers import UserSerializer, NoteSerializer
from rest_framework.viewsets import ModelViewSet
from .models import Profession, GeneralStatistics
from .serializers import ProfessionSerializer, GeneralStatisticsSerializer
from api.models import Note


class NoteListView(generics.ListAPIView):
    serializer_class = NoteSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else :
            serializer.errors = serializer.errors

class NoteDeleteView(generics.DestroyAPIView):
    serializer_class = NoteSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

class ProfessionViewSet(ModelViewSet):
    queryset = Profession.objects.all()
    serializer_class = ProfessionSerializer

class GeneralStatisticsViewSet(ModelViewSet):
    queryset = GeneralStatistics.objects.all()
    serializer_class = GeneralStatisticsSerializer