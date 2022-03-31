from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import OneToOneField

# Create your models here.
class Candidate(models.Model):
    contact = models.CharField(max_length=15)
    image = models.FileField(upload_to="candidate/images", null=True)
    education = models.CharField(max_length=50,null=True)
    experience = models.CharField(max_length=50,null=True)
    skill = models.CharField(max_length=50,null=True)
    gender = models.CharField(max_length=15,null=True)
    birth_date = models.DateField()

    type = models.CharField(max_length=15,null=True)
    user = OneToOneField(User, on_delete=CASCADE,null=True)

    def _str_(self):
        return self.user.username


class Employer(models.Model):
    contact = models.CharField(max_length=15)
    image = models.FileField(upload_to="employer/images", null=True)
    gender = models.CharField(max_length=15,null=True)
    type = models.CharField(max_length=15,null=True)
    company = models.CharField(max_length=25,null=True)
    status = models.CharField(max_length=25,null=True)
    position = models.CharField(max_length=25,null=True)

    user= models.OneToOneField(User, on_delete=CASCADE,null=True)

    def _str_(self):
        return self.user.username


class Job(models.Model):
    title = models.CharField(max_length=50,null=True)
    description = models.CharField(max_length=200,null=True)
    education = models.CharField(max_length=200,null=True)
    post_date = models.DateField()
    deadline = models.DateField()
    salary = models.CharField(max_length=50,null=True)
    vacancy = models.CharField(max_length=50,null=True)
    experience = models.CharField(max_length=100,null=True)
    skill = models.CharField(max_length=100,null=True)
    location = models.CharField(max_length=100,null=True)

    employer= models.ForeignKey(Employer, on_delete=CASCADE,null=True)
    student= models.ManyToManyField(Candidate)

    def _str_(self):
        return self.title