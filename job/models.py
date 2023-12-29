from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from applicants.models import Candidate
from employers.models import Employer


# Create your models here.
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

    employer= models.ForeignKey(Employer, on_delete=CASCADE, null=True)
    student= models.ManyToManyField(Candidate)

    def __str__(self):
        return self.title