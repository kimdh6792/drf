from django.contrib import admin
from .models import *


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    model = User
    list_display = (
        "user_id",
        "email",
        "is_admin",
        "is_active",
        "is_superuser",
        "is_staff",
        "created_on",
        "updated_on",
    )


admin.site.register(User, UserAdmin)
