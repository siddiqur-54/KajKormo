from django.shortcuts import render,redirect
from datetime import date
from applicants.models import Candidate
from job.models import Job
from employers.models import Employer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from datetime import date

# Create your views here.
def admin_login(request):
    error=""
    if request.method=="POST":
        uname= request.POST['username']
        pword= request.POST['password']
        user= authenticate(username=uname, password=pword)
        try:
            if user.is_staff:
                login(request, user)
                error= "no"
            else:
                error="yes"
        except:
            error="yes"
    d={'error': error}
    return render(request, 'admins/admin_login.html',d)


def admin_home(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    user = request.user
    if not user.is_staff:
        return redirect('admin_login')
    error = ""
    if request.method=="POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        user.first_name = fname
        user.last_name = lname
        user.email = email
        try:
            user.save()
            error="no"
        except:
            error="yes"
    d = {'user': user, 'error': error}
    return render(request, 'admins/admin_home.html', d)


def view_users(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    if not request.user.is_staff:
        return redirect('admin_login')
    data = Candidate.objects.all()
    d = {'data': data}
    return render(request, 'admins/view_users.html',d)


def view_employers(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    if not request.user.is_staff:
        return redirect('admin_login')
    data = Employer.objects.filter(status="Approved")
    d = {'data': data}
    return render(request, 'admins/view_employers.html',d)


def view_profile_user(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    candidate = Candidate.objects.get(id=pid)
    d = {'candidate': candidate}
    return render(request, 'admins/view_profile_user.html', d)


def view_profile_employer(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    employer = Employer.objects.get(id=pid)
    d = {'employer': employer}
    return render(request, 'admins/view_profile_employer.html', d)


def delete_user(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    student = User.objects.get(id=pid)
    student.delete()
    return redirect('view_users')


def delete_employer_pending(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    employer = User.objects.get(id=pid)
    employer.delete()
    return redirect('employers_pending')


def delete_employer_approved(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    employer = User.objects.get(id=pid)
    employer.delete()
    return redirect('view_employers')


def approve_employer(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    employer = Employer.objects.get(id=pid)
    employer.status="Approved"
    employer.save()
    return redirect('employers_pending')


def reject_employer(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    employer = Employer.objects.get(id=pid)
    employer.status="Pending"
    employer.save()
    return redirect('view_employers')


def employers_pending(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    data = Employer.objects.filter(status='Pending')
    d = {'data': data}
    return render(request, 'admins/employers_pending.html',d)


def logout_user_admin(request):
    if request.user.is_staff:
        logout(request)
        return redirect('admin_login')
    logout(request)
    return redirect('user_login')


def change_password_admin(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    if not request.user.is_staff:
        return redirect('admin_login')
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
    return render(request, 'admins/change_password_admin.html', d)