from django.contrib import admin

from api.models import Profession, ProfessionImage, GeneralStatistics, GeneralStatisticsImage, GeographyStatistics, GeographyStatisticsImage, DemandStatisticsImage, DemandStatistics, \
    SkillImage, Skill

class ImageInline(admin.TabularInline):
    model = None
    extra = 1
    exclude = ['upload_folder']

    def __init__(self, *args, **kwargs):
        if self.model is None:
            raise ValueError("error")
        super().__init__(*args, **kwargs)


class ProfessionImageInline(ImageInline):
    model = ProfessionImage

class ProfessionAdmin(admin.ModelAdmin):
    inlines = [ProfessionImageInline]

class GeneralStatisticsImageInline(ImageInline):
    model = GeneralStatisticsImage

class GeneralStatisticsAdmin(admin.ModelAdmin):
    inlines = [GeneralStatisticsImageInline]

class SkillImageInline(ImageInline):
    model = SkillImage

class SkillAdmin(admin.ModelAdmin):
    inlines = [SkillImageInline]

class DemandStatisticsImageInline(ImageInline):
    model = DemandStatisticsImage

class DemandStatisticsAdmin(admin.ModelAdmin):
    inlines = [DemandStatisticsImageInline]

class GeographyStatisticsImageInline(ImageInline):
    model = GeographyStatisticsImage

class GeographyStatisticsAdmin(admin.ModelAdmin):
    inlines = [GeographyStatisticsImageInline]

admin.site.register(Profession, ProfessionAdmin)
admin.site.register(ProfessionImage)
admin.site.register(GeneralStatistics, GeneralStatisticsAdmin)
admin.site.register(GeneralStatisticsImage)
admin.site.register(Skill, SkillAdmin)
admin.site.register(SkillImage)
admin.site.register(DemandStatistics, DemandStatisticsAdmin)
admin.site.register(DemandStatisticsImage)
admin.site.register(GeographyStatistics, GeographyStatisticsAdmin)
admin.site.register(GeographyStatisticsImage)