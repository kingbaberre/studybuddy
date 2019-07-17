from django.urls import path
from . import views
urlpatterns = [
    path('home',views.index,name="profile"),
    path('register',views.register,name="register"),
    path('logout',views.logout,name="logout"),
]
