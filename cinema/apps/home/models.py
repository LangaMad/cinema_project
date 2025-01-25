from django.db import models


# Create your models here.

class AboutUs(models.Model):
    title = models.CharField('Title', max_length=200),
    title2 = models.CharField('Title', max_length=200)
    text = models.TextField('Text')
    text2 = models.TextField('Text')
    image1 = models.ImageField('Image', upload_to='images')
    image2 = models.ImageField('Image', upload_to='images')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'О Нас '
        verbose_name_plural = 'О Нас'


class Vacancy(models.Model):
    title = models.CharField('Title', max_length=200)
    text = models.TextField('Text')
    image = models.ImageField('Image', upload_to='images',  blank=True, null=True)
    salary = models.PositiveIntegerField('Salary')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'


class VacancyAnswer(models.Model):
    name = models.CharField('Имя', max_length=200)
    lastname = models.CharField('Фамилия', max_length=200)
    surname = models.CharField('Отчество', blank=True, null=True, max_length=200)
    email = models.EmailField('Электронная почта', max_length=200)
    phone = models.CharField('Телефон', max_length=200)
    birth_year = models.DateField('Год рождения')
    experience = models.PositiveIntegerField('Опыт работы (в годах)', default=0)
    city = models.CharField('Город', max_length=200)
    diploma = models.FileField('Diploma', blank=True, null=True, upload_to='images')
    text = models.TextField('Текст заявки')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ответ на вакансию'
        verbose_name_plural = 'Ответ на вакансии'


class Agreement(models.Model):
    name = models.CharField('Название соглашения', max_length=200)
    content = models.TextField('Текст соглашения')
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)

    @property
    def __str__(self):
        return f'{self.name} - {self.lastname}'

    class Meta:
        verbose_name = 'Соглашение'
        verbose_name_plural = 'Соглашения'
