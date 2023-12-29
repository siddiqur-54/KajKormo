from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from applicants.views import (
    user_login
)

admin.site.site_header = "KajKormo Admin"
admin.site.site_title = "KajKormo Admin Portal"
admin.site.index_title = "Welcome to KajKormo Portal"

urlpatterns = [
    path('applicants/', include('applicants.urls')),
    path('admins/', include('admins.urls')),
    path('employers/', include('employers.urls')),
    path('admin/', admin.site.urls),
    path('', user_login, name="user_login"),
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)