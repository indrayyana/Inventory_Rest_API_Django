from django.urls import path

from user import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('user', views.UserList.as_view()),
    path('user/<id>', views.UserDetail.as_view()),
    
    path('token',TokenObtainPairView.as_view()),
    path('refresh', TokenRefreshView.as_view())
]