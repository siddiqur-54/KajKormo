from django.urls import path
from admins.views import (
    admin_login,
    admin_home,
    view_users,
    view_employers,
    approve_employer,
    delete_user,
    delete_employer_pending,
    delete_employer_approved,
    reject_employer,
    view_profile_user,
    view_profile_employer,
    logout_user_admin,
    change_password_admin,
    employers_pending
)

urlpatterns = [
    path('', admin_login, name="admin_login"),
    path('admin_home', admin_home, name="admin_home"),
    path('view_users', view_users, name="view_users"),
    path('view_employers', view_employers, name="view_employers"),
    path('employers_pending', employers_pending, name="employers_pending"),
    path('approve_employer/<int:pid>', approve_employer, name="approve_employer"),
    path('delete_user/<int:pid>', delete_user, name="delete_user"),
    path('delete_employer_pending/<int:pid>', delete_employer_pending, name="delete_employer_pending"),
    path('delete_employer_approved/<int:pid>', delete_employer_approved, name="delete_employer_approved"),
    path('reject_employer/<int:pid>', reject_employer, name="reject_employer"), 
    path('change_password_admin', change_password_admin, name="change_password_admin"),
    path('logout_user_admin', logout_user_admin, name="logout_user_admin_admin"),
    path('view_profile_user/<int:pid>', view_profile_user, name="view_profile_user"),
    path('view_profile_employer/<int:pid>', view_profile_employer, name="view_profile_employer"),
    path('admin_login', admin_login, name="admin_login"),
]