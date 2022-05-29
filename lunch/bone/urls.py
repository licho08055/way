from django.urls import path

from .views import list_view,detail_view,create_view,update_view,delete_view

app_name = 'bone'
urlpatterns = [
    path('', list_view.as_view(), name='list'),
    path('<int:pk>/', detail_view.as_view(), name='detail'),
    path('create/', create_view.as_view(), name='creates' ),
    path('<int:pk>/update/', update_view.as_view(), name='updates'),
    path('<int:pk>/delete/', delete_view.as_view(), name='deletes'),
]