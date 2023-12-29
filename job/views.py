from django.shortcuts import render,redirect
from datetime import date
from job.models import Candidate
from job.models import Employer, Job
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from datetime import date

# Create your views here.
def add_job(request):
    if not request.user.is_authenticated:
        return redirect('employer_login')
    error = ""
    if request.method=="POST":
        jtitle = request.POST['title']
        desc = request.POST['description']
        edu = request.POST['education']
        deadline = request.POST['deadline']
        sal = request.POST['salary']
        vac = request.POST['vacancy']
        exp = request.POST['experience']
        skl = request.POST['skill']
        loc = request.POST['location']
        user = request.user
        employer = Employer.objects.get(user=user)
        try:
            Job.objects.create(title=jtitle, description=desc, education=edu, deadline=deadline, salary=sal, vacancy=vac, experience=exp, skill=skl, location=loc, post_date=date.today(), employer=employer)
            error="no"
        except:
            error="yes"
    d={'error': error}
    return render(request, 'job/add_job.html',d)


def edit_job(request,pid):
    if not request.user.is_authenticated:
        return redirect('employer_login')
    error = ""
    job = Job.objects.get(id=pid)
    if request.method=="POST":
        jtitle = request.POST['title']
        desc = request.POST['description']
        edu = request.POST['education']
        deadline = request.POST['deadline']
        sal = request.POST['salary']
        vac = request.POST['vacancy']
        exp = request.POST['experience']
        skl = request.POST['skill']
        loc = request.POST['location']

        job.title = jtitle
        job.description = desc
        job.education = edu
        job.salary = sal
        job.vacancy = vac
        job.experience = exp
        job.skill = skl
        job.location = loc
    
        if deadline:
            job.deadline=deadline
        try:
            job.save()
            error="no"
        except:
            error="yes"
    d={'error': error, 'job':job}
    return render(request, 'job/edit_job.html',d)


def delete_job(request,pid):
    if not request.user.is_authenticated:
        return redirect('employer_login')
    job = Job.objects.get(id=pid)
    job.delete()
    return redirect('job_list')


def job_list(request):
    if not request.user.is_authenticated:
        return redirect('employer_login')
    user = request.user
    employer = Employer.objects.get(user=user)
    job = Job.objects.filter(employer=employer)
    d = {'job':job}
    return render(request, 'job/job_list.html', d)


def job_profile_employer(request,pid):
    if not request.user.is_authenticated:
        return redirect('employer_login')
    job = Job.objects.get(id=pid)
    d = {'job': job}
    return render(request, 'job/job_profile_employer.html', d)


def applied_jobs(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    user = request.user
    candidate = Candidate.objects.get(user=user)
    job = Job.objects.filter(student=candidate)
    d = {'job':job}
    return render(request, 'job/applied_jobs.html', d)


def apply_job(request,pid):
    if not request.user.is_authenticated:
        return redirect('user_login')
    user = request.user
    candidate = Candidate.objects.get(user=user)
    job = Job.objects.get(id=pid)
    job.student.add(candidate)
    return redirect('applied_jobs')


def undo_job(request,pid):
    if not request.user.is_authenticated:
        return redirect('user_login')
    user = request.user
    candidate = Candidate.objects.get(user=user)
    job = Job.objects.get(id=pid)
    job.student.remove(candidate)
    return redirect('latest_jobs')


def job_applicants(request,pid):
    if not request.user.is_authenticated:
        return redirect('user_login')
    job = Job.objects.get(id=pid)
    candidate = job.student.all()
    d = {'candidate':candidate}
    return render(request, 'job/job_applicants.html', d)


def latest_jobs(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    user = request.user
    candidate = Candidate.objects.get(user= user)
    job = Job.objects.exclude(student= candidate)
    d = {'job':job}
    return render(request, 'job/latest_jobs.html', d)


def job_profile_user_latest(request,pid):
    if not request.user.is_authenticated:
        return redirect('user_login')
    job = Job.objects.get(id=pid)
    d = {'job': job}
    return render(request, 'job/job_profile_user_latest.html', d)


def job_profile_user_applied(request,pid):
    if not request.user.is_authenticated:
        return redirect('user_login')
    job = Job.objects.get(id=pid)
    d = {'job': job}
    return render(request, 'job/job_profile_user_applied.html', d)