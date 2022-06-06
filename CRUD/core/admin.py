from django.contrib import admin
from core.models import UserTB

# Register your models here.

@admin.register(UserTB)
class UserTBModelAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','password')
    