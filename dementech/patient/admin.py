from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

# Register your models here.
class PatientAdmin(UserAdmin):
    model = Patient
    # list_display = ['email', 'pincode', 'phone','is_staff','is_active']
    # list_filter = ['email', 'pincode', 'phone','is_staff','is_active']
    list_display = ['username','phone_no','doc_code','is_staff','is_active']
    list_filter = ['username','phone_no','doc_code','is_staff','is_active']

    # fieldsets = (
    #     (None, {'fields': ('email', 'password')}),
    #     ('Personal info', {'fields': ('pincode','phone')}),
    #     ('Permissions', {'fields': ('is_active','is_staff')}),
    # )

    fieldsets = (
        (None, {'fields': ('username','phone_no', 'password','doc_code')}),
        ('Permissions', {'fields': ('is_active','is_staff')}),
    )

    # add_fieldsets = (
    #     (None, {
    #         'classes': ('wide,'),
    #         'fields': ('email', 'password1', 'password2', 'phone', 'pincode','is_staff','is_active'),
    #     }),
    # )

    add_fieldsets = (
        (None, {
            'classes': ('wide,'),
            'fields': ('username','phone_no', 'password1', 'password2','doc_code', 'is_staff','is_active'),
        }),
    )
    search_fields = ('username',)
    ordering = ('username',)
    filter_horizontal = ()

admin.site.register(Patient, PatientAdmin)
admin.site.register(Medicine)
admin.site.register(ScrapBook)
admin.site.register(Meme)
