from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "KajKormo Admin"
admin.site.site_title = "KajKormo Admin Portal"
admin.site.index_title = "Welcome to KajKormo Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('job.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)