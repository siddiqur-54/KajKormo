from django.shortcuts import render,redirect
from datetime import date
from applicants.models import Candidate
from job.models import Job
from employers.models import Employer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from datetime import date

# Create your views here.
def employer_signup(request):
    error = ""
    if request.method=="POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        password = request.POST['password']
        gender = request.POST['gender']
        contact = request.POST['contact']
        img = request.FILES['image']
        company = request.POST['company']
        position = request.POST['position']
        email = request.POST['email']
        username = request.POST['email']
           
        try:
            user= User.objects.create_user(username=username,email=email,password=password)
            user.first_name=fname
            user.last_name=lname
            user.save()
            Employer.objects.create(contact=contact, image=img, gender=gender, company=company, position=position, type="employer", status="Pending", user=user)

            error="no"
        except:
            error="yes"
    d={'error': error}
    return render(request, 'employers/employer_signup.html', d)


def employer_login(request):
    error=""
    if request.method=="POST":
        uname= request.POST['username']
        pword= request.POST['password']
        user= authenticate(username=uname, password=pword)
        if user:
            try:
                user1 = Employer.objects.get(user=user)
                if user1.type == "employer" and user1.status=="Approved":
                    login(request,user)
                    error="no"
                else:
                    error="not"
            except:
                error="yes"
        else:
            error="yes"
    d= {'error' : error}
    return render(request, 'employers/employer_login.html',d)


def edit_profile_employer(request):
    if not request.user.is_authenticated:
        return redirect('employer_login')
    user = request.user
    employer = Employer.objects.get(user=user)
    error = ""
    if request.method=="POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        gender = request.POST['gender']
        contact = request.POST['contact']
        company = request.POST['company']
        position = request.POST['position']
        employer.user.first_name = fname
        employer.user.last_name = lname
        employer.gender = gender
        employer.contact = contact
        employer.company = company
        employer.position = position
        try:
            employer.save()
            employer.user.save()
            error="no"
        except:
            error="yes"
    d = {'employer': employer, 'error': error}
    return render(request, 'employers/edit_profile_employer.html', d)


def employer_home(request):
    if not request.user.is_authenticated:
        return redirect('employer_login')
    user = request.user
    employer = Employer.objects.get(user=user)
    d = {'employer': employer}
    return render(request, 'employers/employer_home.html', d)


def view_profile_applicant(request,pid):
    if not request.user.is_authenticated:
        return redirect('employer_login')
    candidate = Candidate.objects.get(id=pid)
    d = {'candidate': candidate}
    return render(request, 'employers/view_profile_applicant.html', d)


def logout_employer(request):
    logout(request)
    return redirect('employer_login')


def delete_employer_own(request):
    if not request.user.is_authenticated:
        return redirect('employer_login')
    employer = request.user
    employer.delete()
    return redirect('employer_login')


def change_password_employer(request):
    if not request.user.is_authenticated:
        return redirect('employer_login')
    e = Employer.objects.get(user = request.user)
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
    return render(request, 'employers/change_password_employer.html', d)