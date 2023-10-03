from django.contrib import admin

# Register your models here.
from .models import *

# admin.site.register(Product)
class UserAdmin (admin.ModelAdmin):
    list_display=["id", "username"]

admin.site.register(User, UserAdmin)