from django.contrib import admin

from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'port', 'expired_date', 'is_expired')
    list_filter = ['expired_date']
    search_fields = ['user_name', 'port']

admin.site.register(User, UserAdmin)
