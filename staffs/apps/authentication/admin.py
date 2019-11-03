
from django.contrib import admin

from staffs.apps.authentication.models import Role, User

admin.site.register(User)
admin.site.register(Role)
