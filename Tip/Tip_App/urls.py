from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('home', views.index, name='home'),
    path('tip', views.tip, name='tip'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('services', views.services, name='services'),
    path('admin/', views.index, name='admin'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('waiters/<int:waiter_id>/', views.waiter_detail, name='waiter_detail'),
    path('waiter/<int:waiter_id>/', views.waiter_detail, name='waiter_detail'),
    path('create_order/<int:waiter_id>/', views.create_order, name='create_order'),
]


