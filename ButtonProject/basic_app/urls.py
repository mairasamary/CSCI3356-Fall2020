from django.urls import path, include
from basic_app import views


urlpatterns = [
    path('index',views.index,name='index'),
    path('system_status',views.system_status,name='system_status'),
    path('change_system_status/<int:system_status_id>/', views.change_system_status, name='change_system_status'),

]
