from django.urls import path
from applicants.views import (
    user_login,
    user_signup,
    user_home,
    delete_user_own,
    change_password_user,
    edit_profile_user
)
from admins.views import (
    logout_user_admin
)
from job.views import (
    applied_jobs,
    latest_jobs,
    apply_job,
    undo_job,
    job_profile_user_latest,
    job_profile_user_applied
)

urlpatterns = [
    path('', user_login, name="user_login"),
    path('user_signup', user_signup, name="user_signup"),
    path('user_home', user_home, name="user_home"),
    path('applied_jobs', applied_jobs, name="applied_jobs"),
    path('latest_jobs', latest_jobs, name="latest_jobs"), 
    path('apply_job/<int:pid>', apply_job, name="apply_job"),
    path('delete_user_own', delete_user_own, name="delete_user_own"),
    path('undo_job/<int:pid>', undo_job, name="undo_job"),
    path('change_password_user', change_password_user, name="change_password_user"),
    path('logout_user_admin', logout_user_admin, name="logout_user_admin_user"),
    path('edit_profile_user', edit_profile_user, name="edit_profile_user"),
    path('job_profile_user_latest/<int:pid>', job_profile_user_latest, name="job_profile_user_latest"),
    path('job_profile_user_applied/<int:pid>', job_profile_user_applied, name="job_profile_user_applied"),
    path('user_login', user_login, name="user_login"),
]