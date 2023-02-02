from django.db import models

# Create your models here.

class Person1(models.Model):
    name = models.CharField(max_length=150,unique=True)
    contact = models.IntegerField()
    birthdate = models.DateField()
    def __str__(self):
        return self.name

class Employee1(models.Model):
    person = models.ForeignKey(Person1, on_delete= models.CASCADE)
    manager = models.CharField(max_length=20)
    salary = models.PositiveBigIntegerField()
    def __str__(self):
        return self.manager
    
class Gender1(models.Model):
    person = models.ForeignKey(Person1, on_delete= models.CASCADE)
    gender_field = models.CharField(max_length=1)
    def __str__(self):
        return self.gender_field
