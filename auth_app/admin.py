from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Contributor, Admin


admin.site.register(Contributor)
admin.site.register(Admin)
