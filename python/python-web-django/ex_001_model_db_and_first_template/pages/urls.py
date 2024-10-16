from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_view, name='home'),
    path('about_admin', views.about_admin_view, name='about_admin'),
    path('about_templates', views.about_templates_view, name='about_templates'),
]
