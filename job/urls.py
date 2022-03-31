from django.contrib import admin
from django.urls import path, include
from job import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.user_login, name="user_login"),
    path('admin_home', views.admin_home, name="admin_home"),
    path('admin_login', views.admin_login, name="admin_login"),

    path('employer_signup', views.employer_signup, name="employer_signup"),
    path('employer_login', views.employer_login, name="employer_login"),
    path('employer_home', views.employer_home, name="employer_home"),
    path('employers_pending', views.employers_pending, name="employers_pending"),

    path('user_login', views.user_login, name="user_login"),
    path('user_signup', views.user_signup, name="user_signup"),
    path('user_home', views.user_home, name="user_home"),
    
    path('add_job', views.add_job, name="add_job"),
    path('applied_jobs', views.applied_jobs, name="applied_jobs"),
    path('job_list', views.job_list, name="job_list"),
    path('latest_jobs', views.latest_jobs, name="latest_jobs"), 
    path('view_users', views.view_users, name="view_users"),
    path('view_employers', views.view_employers, name="view_employers"),

    path('apply_job/<int:pid>', views.apply_job, name="apply_job"),
    path('approve_employer/<int:pid>', views.approve_employer, name="approve_employer"),

    path('delete_user/<int:pid>', views.delete_user, name="delete_user"),
    path('delete_user_own', views.delete_user_own, name="delete_user_own"),

    path('delete_employer_pending/<int:pid>', views.delete_employer_pending, name="delete_employer_pending"),
    path('delete_employer_approved/<int:pid>', views.delete_employer_approved, name="delete_employer_approved"),
    path('delete_employer_own', views.delete_employer_own, name="delete_employer_own"),

    path('delete_job/<int:pid>', views.delete_job, name="delete_job"),

    path('edit_job/<int:pid>', views.edit_job, name="edit_job"),
    path('job_applicants/<int:pid>', views.job_applicants, name="job_applicants"),
    path('reject_employer/<int:pid>', views.reject_employer, name="reject_employer"),
    path('undo_job/<int:pid>', views.undo_job, name="undo_job"),
    
    path('change_password_admin', views.change_password_admin, name="change_password_admin"),
    path('change_password_user', views.change_password_user, name="change_password_user"),
    path('change_password_employer', views.change_password_employer, name="change_password_employer"),
    
    path('logout_employer', views.logout_employer, name="logout_employer"),
    path('logout_user_admin', views.logout_user_admin, name="logout_user_admin"),

    path('edit_profile_employer', views.edit_profile_employer, name="edit_profile_employer"),
    path('edit_profile_user', views.edit_profile_user, name="edit_profile_user"),

    path('view_profile_user/<int:pid>', views.view_profile_user, name="view_profile_user"),
    path('view_profile_employer/<int:pid>', views.view_profile_employer, name="view_profile_employer"),
    path('view_profile_applicant/<int:pid>', views.view_profile_applicant, name="view_profile_applicant"),

    path('job_profile_employer/<int:pid>', views.job_profile_employer, name="job_profile_employer"),
    path('job_profile_user_latest/<int:pid>', views.job_profile_user_latest, name="job_profile_user_latest"),
    path('job_profile_user_applied/<int:pid>', views.job_profile_user_applied, name="job_profile_user_applied"),
]