from rest_framework.viewsets import ModelViewSet
from .models import Profession, GeneralStatistics, DemandStatistics, GeographyStatistics, Skill
from .serializers import ProfessionSerializer, GeneralStatisticsSerializer, GeographyStatisticsSerializer, \
    DemandStatisticsSerializer, SkillSerializer

class ProfessionViewSet(ModelViewSet):
    queryset = Profession.objects.all()
    serializer_class = ProfessionSerializer

class GeneralStatisticsViewSet(ModelViewSet):
    queryset = GeneralStatistics.objects.all()
    serializer_class = GeneralStatisticsSerializer

class SkillViewSet(ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

class DemandStatisticsViewSet(ModelViewSet):
    queryset = DemandStatistics.objects.all()
    serializer_class = DemandStatisticsSerializer

class GeographyStatisticsViewSet(ModelViewSet):
    queryset = GeographyStatistics.objects.all()
    serializer_class = GeographyStatisticsSerializer