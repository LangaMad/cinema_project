from django.db import models

# Create your models here.

class About_us(models.Model):
    title = models.CharField('Title', max_length=200),
    title2 = models.CharField('Title', max_length=200)
    Text = models.TextField('Text')
    Text2 = models.TextField('Text')
    Image1 = models.ImageField('Image',upload_to='images')
    Image2 = models.ImageField('Image',upload_to='images')

class Vacancy(models.Model):
    title = models.CharField('Title', max_length=200),
    Text = models.TextField('Text'),
    image = models.ImageField('Image', upload_to='images')
    Salary = models.IntegerField('Salary'),


class Vacancy_answer(models.Model):
    name = models.CharField('Имя', max_length=200)
    surname = models.CharField('Фамилия', max_length=200)
    lastname = models.CharField('Отчество', max_length=200)
    email = models.EmailField('Электронная почта', max_length=200)
    phone = models.CharField('Телефон', max_length=200)
    birth_year = models.PositiveIntegerField('Год рождения')
    experience = models.PositiveIntegerField('Опыт работы (в годах)', default=0)
    city = models.CharField('Город', max_length=200)
    diploma = models.CharField('Диплом', max_length=200, blank=True, null=True)
    text = models.TextField('Текст заявки')

class Agreement(models.Model):
    name = models.CharField('Название соглашения', max_length=200)
    content = models.TextField('Текст соглашения')
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)

    def __str__(self):
        return self.name



