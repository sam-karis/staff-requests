from django.urls import path

from staffs.apps.staffs.views import (ApproveRequestAPIView,
                                      GetStaffRequestAPIView,
                                      RequestCategoryAPIView,
                                      StaffRequestAPIView)

app_name = 'staffs-requests'

urlpatterns = [
    path('category/', RequestCategoryAPIView.as_view(),
         name='request_category'),
    path('staffs/', StaffRequestAPIView.as_view(), name='staff_requests'),
    path('allstaffs/', GetStaffRequestAPIView.as_view(),
         name='get_staff_requests'),
    path('approve/<request_id>', ApproveRequestAPIView.as_view(),
         name='approve_staff_requests'),
]
