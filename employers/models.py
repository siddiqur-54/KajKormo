from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.
class Employer(models.Model):
    contact = models.CharField(max_length=15)
    image = models.FileField(upload_to="employer/images", null=True)
    gender = models.CharField(max_length=15,null=True)
    type = models.CharField(max_length=15,null=True)
    company = models.CharField(max_length=25,null=True)
    status = models.CharField(max_length=25,null=True)
    position = models.CharField(max_length=25,null=True)

    user= models.OneToOneField(User, on_delete=CASCADE, null=True)

    def __str__(self):
        return self.user.username