from django.urls import path
from . import views


urlpatterns = [

    path('', views.waiter_list, name='waiter_list'),
    path('payment/',views.payment),
    path('admin1/',views.adminlogin),
    # path('add_waiter/', views.add_waiter, name='add_waiter'),
    path('add_waiter/',views.add_waiter),
    
    
]
