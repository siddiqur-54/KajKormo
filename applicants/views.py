from django.shortcuts import render,redirect
from datetime import date
from applicants.models import Candidate
from job.models import Job
from employers.models import Employer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from datetime import date

# Create your views here.
def user_signup(request):
    error = ""
    if request.method=="POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        contact = request.POST['contact']
        img = request.FILES['image']
        education = request.POST['education']
        experience = request.POST['experience']
        skill = request.POST['skill']
        birthdate = request.POST['birthdate']
        gender = request.POST['gender']

        username = request.POST['email']
        try:
            user= User.objects.create_user(username=username,email=email,password=password)
            user.first_name=fname
            user.last_name=lname
            user.save()
            Candidate.objects.create(contact=contact, image=img, education=education, experience=experience, skill=skill, birth_date=birthdate, gender=gender, type="candidate", user=user)
            error="no"
        except:
            error="yes"
    d={'error': error}
    return render(request, 'applicants/user_signup.html',d)


def user_login(request):
    error=""
    if request.method=="POST":
        uname= request.POST['username']
        pword= request.POST['password']
        user= authenticate(username=uname, password=pword)
        if user:
            try:
                user1 = Candidate.objects.get(user=user)
                if user1.type == "candidate":
                    login(request,user)
                    error="no"
                else:
                    error="yes"
            except:
                error="yes"
        else:
            error="yes"
    d= {'error' : error}
    return render(request, 'applicants/user_login.html',d)


def user_home(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    user = request.user
    candidate= Candidate.objects.get(user=user)
    d = {'candidate': candidate}
    return render(request, 'applicants/user_home.html', d)


def edit_profile_user(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    user = request.user
    candidate= Candidate.objects.get(user=user)
    error = ""
    if request.method=="POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        contact = request.POST['contact']
        education = request.POST['education']
        experience = request.POST['experience']
        skill = request.POST['skill']
        birthdate = request.POST['birthdate']
        gender = request.POST['gender']

        candidate.user.first_name = fname
        candidate.user.last_name = lname
        candidate.contact = contact
        candidate.education = education
        candidate.experience = experience
        candidate.skill = skill
        candidate.gender = gender

        if birthdate:
            candidate.birth_date=birthdate

        try:
            candidate.save()
            candidate.user.save()
            error="no"
        except:
            error="yes"
    d = {'candidate': candidate, 'error': error}
    return render(request, 'applicants/edit_profile_user.html', d)


def delete_user_own(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    student = request.user
    student.delete()
    return redirect('user_login')


def change_password_user(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    u = Candidate.objects.get(user = request.user)
    error = ""
    if request.method=="POST":
        currentPass = request.POST['currentpassword']
        newPass = request.POST['newpassword']

        try:
            user = User.objects.get(id=request.user.id)
            if user.check_password(currentPass):
                user.set_password(newPass)
                user.save()
                error="no"
            else:
                error="yeah"
        except:
            error="yes"
    d = {'error': error}
    return render(request, 'applicants/change_password_user.html', d)