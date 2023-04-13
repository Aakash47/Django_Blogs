from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from math import radians, cos, sin, asin, sqrt

class Post(models.Model):
	title = models.CharField(max_length=100)
	slug = models.SlugField(max_length=200, unique=True, default='This Field should be unique')
	content = models.TextField()
	address = models.CharField(max_length=100, default="address")
	lat = models.FloatField(default=0.00000)
	lon = models.FloatField(default=0.00000)
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	image = models.ImageField(null = True, blank = True)

	def __str__(self):
		return self.title

class Acco(models.Model):
	heading = models.CharField(max_length=100)
	desc = models.TextField()
	acco_img = models.ImageField(null = True, blank = True)
	link = models.URLField(default="",max_length=200)

	def __str__(self):
		return self.heading

class Contact(models.Model):
	name = models.CharField(max_length=100, null=False, blank=False)
	mail = models.EmailField(null=False, blank=False)
	desc = models.TextField(null=False, blank=False)
	
	def __str__(self):
		return self.name
