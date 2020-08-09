from django.urls import path
from .views import user_creation_page, login_page, logout_page

urlpatterns = [
    path("signup/", user_creation_page),
    path("login/", login_page),
    path("logout/", logout_page)
]
