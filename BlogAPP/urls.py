from django.urls import path
from BlogAPP import views

urlpatterns = [
    path('', views.home),
    path('viewblog/', views.viewblog),
    path('addblog/', views.addblog),
    path('delete/', views.delete),
    path('deleteid/<int:id>', views.deleteid),
    path('edit/', views.edit),
    path('editid/<int:id>', views.editid),
    path('getid/<int:id>', views.getid),
]
