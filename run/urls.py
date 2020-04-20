from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('login', views.login, name="login"),
    path('logout', views.logout_request, name='logout'),
    path('logincheck',views.login_view, name="logincheck"),
    path('register',views.register_view, name="register"),
    path('dashbord', views.dashbord, name="dashbord"),
    path('contact', views.contact, name="contact")
]
