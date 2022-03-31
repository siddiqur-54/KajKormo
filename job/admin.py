from job.models import Job
from django.contrib import admin
from job.models import Candidate
from job.models import Employer

# Register your models here.

admin.site.register(Candidate)
admin.site.register(Employer)
admin.site.register(Job)