import pytest
from django.test import RequestFactory
from django.urls import reverse


@pytest.fixture
def factory():
    yield RequestFactory()


@pytest.fixture
def urls():
    yield {
        'add_employee': reverse('authentication:add_employee'),
        'login_url': reverse('authentication:login_user'),
        'employee_role_url': reverse('authentication:add_role'),
        'expense_category_url': reverse('staffs-requests:request_category'),
        'staffs_url': reverse('staffs-requests:staff_requests'),
        'allstaffs_url': reverse('staffs-requests:get_staff_requests'),
        'approve_request_url': reverse(
            'staffs-requests:approve_staff_requests', kwargs={'request_id': 1})
    }
