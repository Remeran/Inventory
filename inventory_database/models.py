from __future__ import unicode_literals
from django.core.validators import MaxValueValidator
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.db import models
from datetime import datetime


class Employee(models.Model):
	id = models.PositiveIntegerField(primary_key=True, validators=[MaxValueValidator(9999999)])
	name = models.CharField(max_length=128)
	title = models.CharField(max_length=128)
	department = models.CharField(max_length=128)
	office = models.CharField(max_length=128)
	slug = models.SlugField()

	def __str__(self):
		return self.name
		
	def save(self, *args, **kwargs):
		self.slug = slugify(self.id)
		super(Employee, self).save(*args, **kwargs)

class Lab_Classroom(models.Model):
	room = models.CharField(max_length=128)
	comp_count = models.IntegerField(default=0)
	building = models.CharField(max_length=128)
	dept = models.CharField(max_length=128)
	slug = models.SlugField()

	def __str__(self):
		return self.room

	def save(self, *args, **kwargs):
		self.slug = slugify(self.room)
		super(Lab_Classroom, self).save(*args, **kwargs)
		
	class Meta:
		verbose_name_plural = 'Labs/Classrooms'

# Asset is an abstract class that can be inherited from
class Asset(models.Model):
	SEARCH_CHOICES = (
		(1 , 'Name'),
		(2 , 'Serial'),
		(3 , 'Model'),
		(4 , 'Manufacturer'),
		(5 , 'Assignee - Faculty/Staff'),
		(6 , 'Room - Lab/Classroom'),
		(7 , 'Assignment date'),
		(8 , 'Warranty Expiration date'),
	)
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
	assignee = models.ForeignKey(Employee, blank=True, null=True)
	
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
	license_type = models.CharField(max_length=128)
	license_used = models.IntegerField(default=0)
	
	class Meta:
		verbose_name_plural = 'Software'

class Editor(models.Model):
	user = models.OneToOneField(User)
	is_editor = models.BooleanField(default=False)
	
	def __str__(self): 
		return self.user.username		


