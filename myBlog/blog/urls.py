from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:id>/', views.single, name='single'),     # шаблон, чтобы открывалось сразу по цифре
                                                        # поменять в стиле .../grammatik/nummer/
]