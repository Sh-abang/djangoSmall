from django.urls import path
from . import views


urlpatterns =  [
    path('', views.index, name='index'),
    path('<int:entry_id>/', views.entry, name='entry'),
    path('create/', views.create_entry, name='create_entry'),
    path('edit/<int:entry_id>/',views.edit_entry, name='edit_entry'),
    path('delete/<int:entry_id>/',views.delete,name='delete_entry'),
    path('profile/', views.profile, name='profile'),
]