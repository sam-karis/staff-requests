from django.urls import path

from staffs.apps.authentication.views import LoginUserAPIView, AddUserAPIView

app_name = 'auth'

urlpatterns = [
    path('login/', LoginUserAPIView.as_view(), name='login_user'),
    path('add/', AddUserAPIView.as_view(), name='add_employee'),
]
