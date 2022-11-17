# Register your models here.
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserChangeForm, UserCreationForm
from .models import User


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('id', 'password', 'name', 'email', 'sex', 'addr', 'access_key', 'secret_key', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('id', 'password')}),
        ('Personal info', {'fields': ('name', 'email', 'sex', 'addr', 'access_key', 'secret_key')}),
        ('Permissions', {'fields': ('is_admin',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('id', 'name', 'email', 'sex', 'addr', 'access_key', 'secret_key', 'password1', 'password2')}
         ),
    )
    search_fields = ('id',)
    ordering = ('id',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
