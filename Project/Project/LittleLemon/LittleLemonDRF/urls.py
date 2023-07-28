from django.urls import path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path('message/', views.msg),
    path('api-token-auth/', obtain_auth_token),
    path('menu-items/', views.MenuItemView.as_view()),
    path('menu-items/<int:pk>/', views.SingleItemView.as_view()),
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('book/', views.book, name="book"),
    path('reservations/', views.reservations, name="reservations"),
    path("register", views.register_request, name="register"),
     path("login", views.login_request, name="login"),
    path('menu/', views.menu, name="menu"),
    path('menu_item/<int:pk>/', views.display_menu_item, name="menu_item"),  
    path('bookings/', views.bookings, name="bookings"),
    
    ]
