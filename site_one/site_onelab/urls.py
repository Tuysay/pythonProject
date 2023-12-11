from django.urls import path
from . import views
from .views import BBLoginView, RegisterView, profile, createprofile
from django.contrib.auth import views as authViews

urlpatterns = [
    path('', views.index, name="index"),
    path('createprofile/', createprofile, name='profile'),
    path('profile/', profile, name='profildsa'),
    path('login/', BBLoginView.as_view(), name='login'),
    path('logout/', authViews.LogoutView.as_view(next_page='index'), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
]
