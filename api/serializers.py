from django.contrib.auth.models import User
from rest_framework import serializers
from .models import GeneralStatistics, Profession, ProfessionImage, GeneralStatisticsImage


from rest_framework import serializers
from .models import GeneralStatistics, Profession, ProfessionImage, GeneralStatisticsImage, Skill, SkillImage, DemandStatistics, DemandStatisticsImage, GeographyStatistics, GeographyStatisticsImage

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id', 'image']

class ProfessionImageSerializer(ImageSerializer):
    class Meta(ImageSerializer.Meta):
        model = ProfessionImage

class ProfessionSerializer(serializers.ModelSerializer):
    images = ProfessionImageSerializer(many=True, read_only=True)

    class Meta:
        model = Profession
        fields = ['id', 'name', 'description', 'images']

class GeneralStatisticsImageSerializer(ImageSerializer):
    class Meta(ImageSerializer.Meta):
        model = GeneralStatisticsImage

class GeneralStatisticsSerializer(serializers.ModelSerializer):
    images = GeneralStatisticsImageSerializer(many=True, read_only=True)

    class Meta:
        model = GeneralStatistics
        fields = ['id', 'description', 'images']

class SkillImageSerializer(ImageSerializer):
    class Meta(ImageSerializer.Meta):
        model = SkillImage

class SkillSerializer(serializers.ModelSerializer):
    images = SkillImageSerializer(many=True, read_only=True)

    class Meta:
        model = Skill
        fields = ['id', 'description', 'images']

class DemandStatisticsImageSerializer(ImageSerializer):
    class Meta(ImageSerializer.Meta):
        model = DemandStatisticsImage

class DemandStatisticsSerializer(serializers.ModelSerializer):
    images = DemandStatisticsImageSerializer(many=True, read_only=True)

    class Meta:
        model = DemandStatistics
        fields = ['id', 'description', 'images']

class GeographyStatisticsImageSerializer(ImageSerializer):
    class Meta(ImageSerializer.Meta):
        model = GeographyStatisticsImage

class GeographyStatisticsSerializer(serializers.ModelSerializer):
    images = GeographyStatisticsImageSerializer(many=True, read_only=True)

    class Meta:
        model = GeographyStatistics
        fields = ['id', 'description', 'images']

