from django.urls import path
from . import views

urlpatterns = [
    path('', views.service_request_list, name='service_request_list'),
    path('new/', views.service_request_create, name='service_request_new'),
    path('<int:pk>/', views.service_request_detail, name='service_request_detail'),
    path('<int:pk>/edit/', views.service_request_update, name='service_request_edit'),
    path('<int:pk>/delete/', views.service_request_delete, name='service_request_delete'),
]

