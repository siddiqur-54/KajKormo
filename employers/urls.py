from django.urls import path
from job.views import (
    add_job,
    job_list,
    delete_job,
    edit_job,
    job_profile_employer,
    job_applicants

)
from applicants import views
from employers.views import (
    employer_login,
    employer_signup,
    employer_home,
    change_password_employer,
    logout_employer,
    edit_profile_employer,
    view_profile_applicant,
    delete_employer_own
)

urlpatterns = [
    path('', employer_login, name="employer_login"),
    path('employer_signup', employer_signup, name="employer_signup"),
    path('employer_home', employer_home, name="employer_home"),
    path('add_job', add_job, name="add_job"),
    path('job_list', job_list, name="job_list"),
    path('delete_employer_own', delete_employer_own, name="delete_employer_own"),
    path('delete_job/<int:pid>', delete_job, name="delete_job"),
    path('edit_job/<int:pid>', edit_job, name="edit_job"),
    path('job_applicants/<int:pid>', job_applicants, name="job_applicants"),
    path('change_password_employer', change_password_employer, name="change_password_employer"),
    path('logout_employer', logout_employer, name="logout_employer"),
    path('edit_profile_employer', edit_profile_employer, name="edit_profile_employer"),
    path('view_profile_applicant/<int:pid>', view_profile_applicant, name="view_profile_applicant"),
    path('job_profile_employer/<int:pid>', job_profile_employer, name="job_profile_employer"),
    path('employer_login', employer_login, name="employer_login"),
]