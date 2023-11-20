from django.urls import path, include
from .views import UserLogin, UserSignup, UserLogout, UserView

urlpatterns = [
  path('', include('djoser.urls')),
  path('', include('djoser.urls.authtoken')),
  path("signup/", UserSignup.as_view(), name="signup"),
  path("login/", UserLogin.as_view(), name="login"),
  path("logout/", UserLogout.as_view(), name="logout"),
  path("user/", UserView.as_view(), name="user"),
  
]

