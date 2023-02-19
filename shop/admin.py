from django.contrib import admin
from .models import *


from .forms import *
from django.contrib.auth.admin import UserAdmin


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

    list_display = ('id', 'email', 'username')
    list_display_links = ('username',)

    fieldsets = UserAdmin.fieldsets + (
        (
            None, {
                'fields': ('address', 'postcode', 'city', 'phone')
            }
        ),
    )


    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            None,
            {
                'fields': ('first_name', 'last_name', 'email', 'address', 'postcode', 'city', 'phone')
            }
        ),
    )

    ordering = ('id',)


