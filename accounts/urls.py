from django.urls import path
from . import views


urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("profile/", views.profile, name="profile"),
    path("register/", views.register_user, name="register"),
]
