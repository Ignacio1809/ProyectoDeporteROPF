from django.urls import path
from authapp import views

urlpatterns = [
    path('', views.Home, name="Home"),
    path('plans', views.all_plans, name="all_plans"),
    path('signup', views.signup, name="signup"),
    path('login', views.handlelogin, name="handlelogin"),
    path('logout', views.handleLogout, name="handleLogout"),
    path('plans/<int:Plan_id>/', views.single_plan, name="single_plan"),
 
]
