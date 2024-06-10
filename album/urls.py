
from django.urls import path

from .import views

urlpatterns = [
 
  
    path('listng/',views.add_album,name='add_album'),
    path('editing<int:id>',views.edit_album,name='edit_album'),
    path('delete <int:id>',views.delete_album,name='delete_album')

]