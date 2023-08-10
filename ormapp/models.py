from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Cource(models.Model):
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE)
    cource_name = models.CharField(max_length=200)
    price = models.IntegerField()
    
    def __str__(self):
        return self.cource_name


class Lesson(models.Model):
    lesson_name = models.CharField(max_length=200)
    cource = models.ForeignKey(Cource,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.lesson_name



class Chapter(models.Model):
    chapter_name = models.CharField(max_length=200)
    lesson = models.ForeignKey(Lesson,on_delete=models.CASCADE)
    index_number = models.IntegerField()

    def __str__(self):
        return self.chapter_name