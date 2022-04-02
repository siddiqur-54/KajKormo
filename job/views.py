from django.shortcuts import render,redirect
from datetime import date
from job.models import Candidate
from job.models import Employer, Job
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from datetime import date


# Create your views here.

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
    return render(request, 'admin_home.html', d)


def user_home(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    user = request.user
    candidate= Candidate.objects.get(user=user)
    d = {'candidate': candidate}
    return render(request, 'user_home.html', d)


def view_profile_user(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    candidate = Candidate.objects.get(id=pid)
    d = {'candidate': candidate}
    return render(request, 'view_profile_user.html', d)


def view_profile_employer(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    employer = Employer.objects.get(id=pid)
    d = {'employer': employer}
    return render(request, 'view_profile_employer.html', d)


def view_profile_applicant(request,pid):
    if not request.user.is_authenticated:
        return redirect('employer_login')
    candidate = Candidate.objects.get(id=pid)
    d = {'candidate': candidate}
    return render(request, 'view_profile_applicant.html', d)


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
    return render(request, 'edit_profile_user.html', d)


def employer_home(request):
    if not request.user.is_authenticated:
        return redirect('employer_login')
    user = request.user
    employer = Employer.objects.get(user=user)
    d = {'employer': employer}
    return render(request, 'employer_home.html', d)


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
    return render(request, 'edit_profile_employer.html', d)


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
    return render(request, 'admin_login.html',d)


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
    return render(request, 'user_login.html',d)


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
    return render(request, 'employer_login.html',d)


def logout_user_admin(request):
    if request.user.is_staff:
        logout(request)
        return redirect('admin_login')
    logout(request)
    return redirect('user_login')


def logout_employer(request):
    logout(request)
    return redirect('employer_login')


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
    return render(request, 'user_signup.html',d)


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
    return render(request, 'employer_signup.html', d)


def view_users(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    if not request.user.is_staff:
        return redirect('admin_login')
    data = Candidate.objects.all()
    d = {'data': data}
    return render(request, 'view_users.html',d)


def view_employers(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    if not request.user.is_staff:
        return redirect('admin_login')
    data = Employer.objects.filter(status="Approved")
    d = {'data': data}
    return render(request, 'view_employers.html',d)


def delete_user(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    student = User.objects.get(id=pid)
    student.delete()
    return redirect('view_users')


def delete_user_own(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    student = request.user
    student.delete()
    return redirect('user_login')


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


def delete_employer_own(request):
    if not request.user.is_authenticated:
        return redirect('employer_login')
    employer = request.user
    employer.delete()
    return redirect('employer_login')
    

def delete_job(request,pid):
    if not request.user.is_authenticated:
        return redirect('employer_login')
    job = Job.objects.get(id=pid)
    job.delete()
    return redirect('job_list')


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
    return render(request, 'employers_pending.html',d)


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
    return render(request, 'add_job.html',d)


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
    return render(request, 'edit_job.html',d)


def job_list(request):
    if not request.user.is_authenticated:
        return redirect('employer_login')
    user = request.user
    employer = Employer.objects.get(user=user)
    job = Job.objects.filter(employer=employer)
    d = {'job':job}
    return render(request, 'job_list.html', d)


def applied_jobs(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    user = request.user
    candidate = Candidate.objects.get(user=user)
    job = Job.objects.filter(student=candidate)
    d = {'job':job}
    return render(request, 'applied_jobs.html', d)


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
    return render(request, 'job_applicants.html', d)


def latest_jobs(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    user = request.user
    candidate = Candidate.objects.get(user= user)
    job = Job.objects.exclude(student= candidate)
    d = {'job':job}
    return render(request, 'latest_jobs.html', d)


def job_profile_employer(request,pid):
    if not request.user.is_authenticated:
        return redirect('employer_login')
    job = Job.objects.get(id=pid)
    d = {'job': job}
    return render(request, 'job_profile_employer.html', d)


def job_profile_user_latest(request,pid):
    if not request.user.is_authenticated:
        return redirect('user_login')
    job = Job.objects.get(id=pid)
    d = {'job': job}
    return render(request, 'job_profile_user_latest.html', d)


def job_profile_user_applied(request,pid):
    if not request.user.is_authenticated:
        return redirect('user_login')
    job = Job.objects.get(id=pid)
    d = {'job': job}
    return render(request, 'job_profile_user_applied.html', d)


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
    return render(request, 'change_password_admin.html', d)


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
    return render(request, 'change_password_user.html', d)


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
    return render(request, 'change_password_employer.html', d)