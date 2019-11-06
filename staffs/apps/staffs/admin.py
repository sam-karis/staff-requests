
from django.contrib import admin

from staffs.apps.staffs.models import RequestsCategory, StaffRequest

admin.site.register(RequestsCategory)
admin.site.register(StaffRequest)
