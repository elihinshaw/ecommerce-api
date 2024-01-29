from django.urls import path
from .views import UserList, UserDetails, ProtectedResourceView
from rest_framework_simplejwt import views as jwt_views
from .views import SignupView


urlpatterns = [
    path("protected-resource/", ProtectedResourceView.as_view(), name="hello_world"),
    path("token/", jwt_views.TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", jwt_views.TokenRefreshView.as_view(), name="token_refresh"),
    path("signup/", SignupView.as_view(), name="signup"),
    path("users/", UserList.as_view(), name="user-list"),
    path("users/<pk>/", UserDetails.as_view(), name="user-detail"),
]
