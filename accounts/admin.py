from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin, GroupAdmin as BaseGroupAdmin
from django.contrib.auth.models import User, Group

from unfold.admin import ModelAdmin

from accounts import models, forms


# admin.site.unregister(User)
admin.site.unregister(Group)


@admin.register(models.User)
class UserAdmin(BaseUserAdmin, ModelAdmin):
    form = forms.UserChangeForm
    add_form = forms.UserCreationForm
    change_password_form = forms.AdminPasswordChangeForm

    list_display = ['username', 'is_staff']
    list_filter = ['is_staff']

    search_fields = ['username']

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Права доступа', {
            'fields': ('is_staff', 'is_superuser', 'groups', 'user_permissions')
        }),
        ('Важные даты', {'fields': ('last_login',)})
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'is_staff', 'is_superuser', 'groups')
        }),
    )


@admin.register(Group)
class GroupAdmin(BaseGroupAdmin, ModelAdmin):
    pass
