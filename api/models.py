from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')

    def __str__(self):
        return self.title


class Profession(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='profession_images/', blank=True, null=True)

    def __str__(self):
        return self.name


class GeneralStatistics(models.Model):
    year = models.PositiveIntegerField()
    average_salary_rub = models.FloatField()
    total_vacancies = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.year} - Avg Salary: {self.average_salary_rub}"


class CitySalary(models.Model):
    city = models.CharField(max_length=100)
    average_salary_rub = models.FloatField()
    total_vacancies = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.city} - {self.average_salary_rub} RUB"


class Skill(models.Model):
    name = models.CharField(max_length=100, unique=True)
    frequency = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class SkillByYear(models.Model):
    year = models.PositiveIntegerField()
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name='skill_years')
    frequency = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.skill.name} ({self.year})"

# Модель для хранения вакансий из API HH
class Vacancy(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    skills = models.TextField()
    company = models.CharField(max_length=200)
    salary_from = models.FloatField(blank=True, null=True)
    salary_to = models.FloatField(blank=True, null=True)
    currency = models.CharField(max_length=10, blank=True, null=True)
    region = models.CharField(max_length=200)
    published_at = models.DateTimeField()

    def __str__(self):
        return self.title

# Модель для аналитики по востребованности профессии
class DemandStatistics(models.Model):
    year = models.PositiveIntegerField()
    profession = models.ForeignKey(Profession, on_delete=models.CASCADE)
    average_salary_rub = models.FloatField()
    total_vacancies = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.profession.name} ({self.year})"


class GeographyStatistics(models.Model):
    city = models.CharField(max_length=100)
    profession = models.ForeignKey(Profession, on_delete=models.CASCADE)
    average_salary_rub = models.FloatField()
    vacancies_share = models.FloatField()

    def __str__(self):
        return f"{self.city} - {self.profession.name}"

