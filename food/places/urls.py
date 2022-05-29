from django.urls import path
from . import views


app_name = 'places'
urlpatterns = [
    path('', views.place_list, name='place-list'),
    path('<int:place_id>/', views.place_detail, name='place-detail'),
    path('create/', views.place_create, name='place-create'),
    path('update/<int:place_id>/', views.place_update, name='place-update'),
    path('delete/<int:place_id>/', views.place_delete, name='place-delete')
]