from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

admin.autodiscover()  # функция автоматического обнаружения файлов admin.py в наших приложениях

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^grammar/', include('gramm.urls')),
]
