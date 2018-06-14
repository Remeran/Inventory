from __future__ import unicode_literals
from django.core.validators import MaxValueValidator
from django.template.defaultfilters import slugify
from django.db import models
from datetime import datetime


class Employee(models.Model):
    id = models.PositiveIntegerField(primary_key=True, validators=[MaxValueValidator(9999999)])
    name = models.CharField(max_length=128)
    title = models.CharField(max_length=128)
    department = models.CharField(max_length=128)
    office = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Lab_Classroom(models.Model):
    room = models.CharField(max_length=128)
    comp_count = models.IntegerField(default=0)
    building = models.CharField(max_length=128)
    dept = models.CharField(max_length=128)

    def __str__(self):
        return self.room
		
    class Meta:
        verbose_name_plural = 'Labs/Classrooms'

# Asset is an abstract class that can be inherited from
class Asset(models.Model):
    name = models.CharField(max_length=128, unique=True)
    slug = models.SlugField()

	
    class Meta:
		abstract = True
		
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Asset, self).save(*args, **kwargs)

# Hardware is an abstract class that inherits from the Asset class	
class Hardware(Asset):
    serial = models.CharField(max_length=128, unique=True)
    manufacturer = models.CharField(max_length=128)
    model = models.CharField(max_length=128)
    war_exp = models.DateField()
    date_assigned = models.DateField()

    class Meta:
        abstract = True
# Fac is a class that inherits from	Hardware and Assets	
class Fac(Hardware):
    asignee = models.ForeignKey(Employee)
	
    class Meta:
        verbose_name_plural = 'Faculty/Staff Computers'	

class Student(Hardware):
    room = models.ForeignKey(Lab_Classroom)
    class Meta:
        verbose_name_plural = 'Student Computers'	

# Software is a class that inherits from Assets			
class Software(Asset):
    developer = models.CharField(max_length=128)
    lic_exp = models.DateField()
    assigned_dept = models.CharField(max_length=128)
    lisence_type = models.CharField(max_length=128)
    date_assigned = models.DateField()
    license_used = models.IntegerField(default=0)
	
    class Meta:
        verbose_name_plural = 'Software'	

