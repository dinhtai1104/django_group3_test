from email.mime import image
from email.policy import default
from enum import auto
from pyexpat import model
from statistics import mode
from unicodedata import category, name
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200)

	def __str__(self):
		return self.name

# class Author(models.Model):
# 	name = models.CharField(max_length=200, primary_key=True)

# class CategoryBook(models.Model):
# 	name = models.CharField(max_length=200, primary_key=True)


# class Book(models.Model):
# 	id = models.IntegerField(primary_key=True, auto_created=True)
# 	name = models.CharField(max_length=200)
# 	price = models.FloatField()
# 	author=models.ForeignKey(Author.name, on_delete=models.SET_NULL, null=True)
# 	category=models.ForeignKey(CategoryBook.name, on_delete=models.SET_NULL, null=True)
# 	saleoff=models.FloatField()


# class Brand(models.Model):
# 	name = models.CharField(max_length=200)

# class MobilePhone(models.Model):
# 	id = models.IntegerField(primary_key=True, auto_created=True)
# 	name = models.CharField(max_length=200)
# 	price = models.FloatField()
# 	brand = models.ForeignKey(Brand.name, on_delete=models.SET_NULL, null=True)

# class Laptop(models.Model):
# 	id = models.IntegerField(primary_key=True, auto_created=True)
# 	name = models.CharField(max_length=200)
# 	price = models.FloatField()
# 	ram = models.IntegerField()
# 	ssd = models.BooleanField()
# 	brand = models.ForeignKey(Brand.name, on_delete=models.SET_NULL, null=True)

# class Clothes(models.Model):
# 	id = models.IntegerField(primary_key=True, auto_created=True)
# 	name = models.CharField(max_length=200)
# 	price = models.FloatField()
# 	brand = models.ForeignKey(Brand.name, on_delete=models.SET_NULL, null=True)

# class Shoes(models.Model):
# 	id = models.IntegerField(primary_key=True, auto_created=True)
# 	name = models.CharField(max_length=200)
# 	price = models.FloatField()
# 	brand = models.ForeignKey(Brand.name, on_delete=models.SET_NULL, null=True)

# class Electronics(models.Model):
# 	id = models.IntegerField(primary_key=True, auto_created=True)
# 	name = models.CharField(max_length=200)
# 	price = models.FloatField()
# 	brand = models.ForeignKey(Brand.name, on_delete=models.SET_NULL, null=True)


class Product(models.Model):
	name = models.CharField(max_length=200)
	price = models.FloatField()
	digital = models.BooleanField(default=False,null=True, blank=True)
	image = models.ImageField(default="")
	def __str__(self):
		return self.name

	@property
	def imageURL(self):
		try:
			url = self.image.url
		except:
			url = ''
		return url
class Order(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
	date_ordered = models.DateTimeField(auto_now_add=True)
	complete = models.BooleanField(default=False)
	transaction_id = models.CharField(max_length=100, null=True)

	def __str__(self):
		return str(self.id)

class OrderItem(models.Model):
	product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	quantity = models.IntegerField(default=0, null=True, blank=True)
	date_added = models.DateTimeField(auto_now_add=True)

class Test(models.Model):
	name=models.CharField(max_length=200)