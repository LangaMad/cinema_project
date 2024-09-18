from django.contrib import admin

from .models import Vacancy, Agreement, AboutUs, VacancyAnswer


# Register your models here.
@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    objects = None
    list_display = [
        'title',
        'title2',
        'text',
        'text2',
        'image',
        'image2',
    ]


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'text',
        'image',
        'salary'
    ]


@admin.register(VacancyAnswer)
class VacancyAnswerAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'lastname',
        'surname',
        'email',
        'phone',
        'birth_year',
        'experience',
        'city',
        'diploma',
        'text'
    ]

@admin.register(Agreement)
class AgreementAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'content',
        'created_at',
    ]