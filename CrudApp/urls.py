from django import urls
from django.urls import path
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, logout_then_login
from . import views

urlpatterns = [
    path('', login_required(views.home), name='home'),
    path('add', views.new, name='new'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('accounts/login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', logout_then_login, name='logout'),
]
