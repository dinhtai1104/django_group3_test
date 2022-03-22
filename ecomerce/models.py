from email.mime import image
from email.policy import default
from enum import auto
from pyexpat import model
from statistics import mode
from unicodedata import category, name
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
	name= models.CharField(max_length=255)
	author= models.CharField(max_length=255)
	language= models.CharField(max_length=255)
	expressed_year= models.CharField(max_length=255)
	size= models.CharField(max_length=255)
	image = models.ImageField(default="")
	price= models.IntegerField()
	@property
	def imageURL(self):
		try:
			url = self.image.url
		except:
			url = ''
		return url

class MobilePhone(models.Model):
	name= models.CharField(max_length=255)
	publicationYear= models.IntegerField()
	manufacture= models.CharField(max_length=255)
	storage= models.CharField(max_length=255)
	ram= models.CharField(max_length=255)
	price= models.IntegerField()
	color= models.CharField(max_length=255)
	image = models.ImageField(default="")
	@property
	def imageURL(self):
		try:
			url = self.image.url
		except:
			url = ''
		return url
	def __str__(self) -> str:
		return str(self.name)
        
class Clothes(models.Model):
	color=models.CharField(max_length=255)
	size= models.IntegerField()
	manufacture=models.CharField(max_length=255)
	material= models.CharField(max_length=255)
	name= models.CharField(max_length=255)
	price= models.IntegerField(default=19)
	image = models.ImageField(default="")
	@property
	def imageURL(self):
		try:
			url = self.image.url
		except:
			url = ''
		return url
	def __str__(self) -> str:	
		return str(self.name)

class Laptop(models.Model):
	name= models.CharField(max_length=255)
	publicationYear= models.IntegerField()
	manufacture= models.CharField(max_length=255)
	storage= models.CharField(max_length=255)
	ram= models.CharField(max_length=255)
	color= models.CharField(max_length=255)
	type=models.CharField(max_length=255)
	chip= models.CharField(max_length=255)
	image = models.ImageField(default="")
	price= models.IntegerField()
	@property
	def imageURL(self):
		try:
			url = self.image.url
		except:
			url = ''
		return url
	def __str__(self) -> str:
		return str(self.name)

class Shoes(models.Model):
	color=models.CharField(max_length=255)
	size= models.IntegerField()
	manufacture=models.CharField(max_length=255)
	material= models.CharField(max_length=255)
	name= models.CharField(max_length=255)
	image = models.ImageField(default="")
	price= models.IntegerField()
	@property
	def imageURL(self):
		try:
			url = self.image.url
		except:
			url = ''
		return url
	def __str__(self) -> str:
		return str(self.name)

class Electronic(models.Model):
	name=models.CharField(max_length=255)
	publicationYear= models.IntegerField()
	type= models.CharField(max_length=255)
	image = models.ImageField(default="")
	price= models.IntegerField()
	@property
	def imageURL(self):
		try:
			url = self.image.url
		except:
			url = ''
		return url
	def __str__(self) -> str:
		return str(self.name)