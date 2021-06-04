from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_admin=models.BooleanField(default=False)
    is_student=models.BooleanField(default=False)
    is_teacher=models.BooleanField(default=False)

class student(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    department=models.CharField(max_length=80)

class teacher(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    department=models.CharField(max_length=80)

class EbookModel(models.Model):
	title=models.CharField(max_length=60)
	pdf=models.FileField(upload_to='pdfs/',blank=True)

	class Meta(object):
		ordering=['title']
	def __str__(self):
		return f"{self.title}"
class EbookModel2(models.Model):
	title=models.CharField(max_length=60)
	pdf=models.FileField(upload_to='pdfs/',blank=True)

	class Meta(object):
		ordering=['title']
	def __str__(self):
		return f"{self.title}"

class EbookModel3(models.Model):
	title=models.CharField(max_length=60)
	pdf=models.FileField(upload_to='pdfs/',blank=True)

	class Meta(object):
		ordering=['title']
	def __str__(self):
		return f"{self.title}"

class EbookModel4(models.Model):
	title=models.CharField(max_length=60)
	pdf=models.FileField(upload_to='pdfs/',blank=True)

	class Meta(object):
		ordering=['title']
	def __str__(self):
		return f"{self.title}"

class FeedBack(models.Model):
	name=models.CharField(max_length=20)
	feedback=models.TextField()
	username=models.CharField(max_length=20)


	class Meta:
		ordering=['name']	

	def __str__(self):
		return f"feedback by {self.name}"		
		