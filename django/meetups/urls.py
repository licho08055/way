from django.urls import path
from .import views


urlpatterns = [
    path('', views.index, name='all-meetup'),
    path('<slug:meetup_slug>/success', views.confirm_registration, name='confirm-registration'),
    path('<slug:meetup_slug>', views.meetup_detail, name='meetup-detail'),
    
]