from django.urls import path
from . import views

urlpatterns = [
        path('', views.home, name='home'),
        path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
        path('create_student/', views.create_student, name='create_student'),
        path('create_tutor/', views.create_tutor, name='create_tutor'),
        path('tutor_login/', views.tutor_login, name='tutor_login')
        ]
