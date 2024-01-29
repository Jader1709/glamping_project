from . import views
from django.urls import path

urlpatterns = [      
    path('', views.tipo_cabañas, name='tipo_cabañas'),  
     path('tipo_cabaña_status_/<int:tipo_cabaña_id>/', views.change_status_tipo_cabaña, name='tipo_cabaña_status'),          
     path('create/', views.create_tipo_cabaña, name='create_tipo_cabaña'), 
]