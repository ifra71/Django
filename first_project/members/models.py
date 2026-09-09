from django.db import models
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError


def validate_phone(value):
    if not value.startswith("03"):
        raise ValidationError("Phone number must start with 03.")


class Members(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.IntegerField(
        validators = [MinValueValidator(18)]
    )
    phone_number = models.CharField(
        max_length = 11,
        validators = [validate_phone]
    )

    nickname = models.CharField(
        max_length=50,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ["name"]
       


class Course(models.Model):
    name = models.CharField(max_length=100)

class PhoneNumberField(models.CharField):

    def __init__(self, *args, **kwargs):
        kwargs["max_length"] = 11
        super().__init__(*args, **kwargs)

class Student(models.Model):
    name = models.CharField(max_length=100)
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE
    )
    phone = PhoneNumberField()



class Passport(models.Model):
    number = models.CharField(max_length=20)

class Person(models.Model):
    name = models.CharField(max_length=100)
    passport = models.OneToOneField(
        Passport,
        on_delete=models.CASCADE
    )