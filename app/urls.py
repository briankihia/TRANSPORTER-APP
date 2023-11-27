from django.urls import path
from .import views

urlpatterns = [
    # whenever someone calls for the homepage
    # the views.home is calling the function home in views.
    path('', views.firstPage, name='firstPage'),
     path('home/', views.home, name='home'),
     path('sender/', views.sender, name='sender'),
     path('transporter/', views.transporter, name='transporter'),
     path('orders/', views.orders, name='orders'),
     path('workerPage/', views.workerPage, name='workerPage'),
     path('order_details/<int:order_id>/', views.order_details, name='order_details'),
     path('update_online_status', views.update_online_status, name='update_online_status'),
     path('map', views.map, name='map')
]