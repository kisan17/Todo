from django.urls import path
from . import views 

urlpatterns = [
    path('showall',views.showall,name='showall'),
    path('detail/<int:id>/',views.detail,name='detail'),
    path('update/<int:id>/',views.Update,name='update'),
    path('create/',views.create,name='create'),
    path('delete<int:id>/',views.delete,name='delete'),
    
   
]