import os
import random
import string

from django.db import models
from django.utils.text import get_valid_filename, slugify

def image_upload_path(instance, filename):
    base, ext = os.path.splitext(filename)
    safe_name = slugify(base)

    subfolder = instance.upload_folder

    return os.path.join(subfolder, f'{safe_name}{ext}')

class Profession(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name

class ImageBase(models.Model):
    upload_folder = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to=image_upload_path)

    class Meta:
        abstract = True

    def __str__(self):
        return self.__class__.__name__

class ProfessionImage(ImageBase):
    image = models.ImageField(upload_to=image_upload_path)
    profession = models.ForeignKey(Profession, on_delete=models.CASCADE, related_name='images')

    def save(self, *args, **kwargs):
        if not self.upload_folder:
            self.upload_folder = 'profession_images'
        super().save(*args, **kwargs)

class GeneralStatistics(models.Model):
    description = models.TextField(default="")

    def __str__(self):
        return self.description

class GeneralStatisticsImage(ImageBase):
    image = models.ImageField(upload_to=image_upload_path)
    general_statistics = models.ForeignKey(GeneralStatistics, on_delete=models.CASCADE, related_name='images')

    def save(self, *args, **kwargs):
        if not self.upload_folder:
            self.upload_folder = 'general_statistics'
        super().save(*args, **kwargs)

class Skill(models.Model):
    description = models.TextField(default="")

    def __str__(self):
        return self.description

class SkillImage(ImageBase):
    image = models.ImageField(upload_to=image_upload_path)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name='images')

    def save(self, *args, **kwargs):
        if not self.upload_folder:
            self.upload_folder = 'skill'
        super().save(*args, **kwargs)

class DemandStatistics(models.Model):
    description = models.TextField(default="")

    def __str__(self):
        return self.description

class DemandStatisticsImage(ImageBase):
    image = models.ImageField(upload_to=image_upload_path)
    demand_statistics = models.ForeignKey(DemandStatistics, on_delete=models.CASCADE, related_name='images')

    def save(self, *args, **kwargs):
        if not self.upload_folder:
            self.upload_folder = 'demand_statistics'
        super().save(*args, **kwargs)

class GeographyStatistics(models.Model):
    description = models.TextField(default="")

    def __str__(self):
        return self.description

class GeographyStatisticsImage(ImageBase):
    image = models.ImageField(upload_to=image_upload_path)
    geography_statistics = models.ForeignKey(GeographyStatistics, on_delete=models.CASCADE, related_name='images')

    def save(self, *args, **kwargs):
        if not self.upload_folder:
            self.upload_folder = 'geography_statistics'
        super().save(*args, **kwargs)

