from django.db import models
from django.core.validators import MinValueValidator

class Member(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.IntegerField(null=True)
    age = models.IntegerField(
        validators = [MinValueValidator(18)]
    )

    @property
    def full_details(self):
        return self.first_name+" "+ self.last_name

#foreign
class Student(models.Model):
    name = models.CharField(max_length=255)
    
class Subjects(models.Model):
    title = models.CharField(max_length=255)
    student = models.ForeignKey(
        Student,
        on_delete = models.CASCADE
    )
#manytomany
class Course(models.Model):
    course = models.CharField(max_length=223)
    students = models.ManyToManyField(Student)

#onetoone

class Person(models.Model):
    name = models.CharField(max_length=203)

class Passport(models.Model):
    person = models.OneToOneField(
        Person,
        on_delete = models.CASCADE
    )


class Dishes(models.Model):
    dish_name = models.CharField(max_length=255)

    class Meta:
        ordering = ["dish_name"]


class Calculator:

    @staticmethod
    def add(a, b):
        return a + b

class Sdent:
    school = "UET"

    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def change_school(cls, name):
        cls.school = name

#custom fields

class PhoneNumberField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("max_length", 15)
        super().__init__(*args, **kwargs)
