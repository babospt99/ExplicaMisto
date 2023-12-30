# urls.py
from django.urls import path
from .views import HomeView

urlpatterns = [
    path("", HomeView.home),
    path("logout", HomeView.logout_view)
]
