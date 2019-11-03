from django.urls import path

from staffs.apps.authentication.views import (AddUserAPIView, LoginUserAPIView,
                                              RoleAPIView)

app_name = 'auth'

urlpatterns = [
    path('login/', LoginUserAPIView.as_view(), name='login_user'),
    path('add/', AddUserAPIView.as_view(), name='add_employee'),
    path('addrole/', RoleAPIView.as_view(), name='add_role'),
]
