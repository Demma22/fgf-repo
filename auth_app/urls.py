# urls.py
from django.urls import path
from .views import UserCreateView, UserRetrieveView

urlpatterns = [
    path("users/", UserCreateView.as_view(), name="user-create"),
    path("users/<int:pk>/", UserRetrieveView.as_view(), name="user-retrieve"),
]
