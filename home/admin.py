from django.contrib import admin
from home.models import savings,user_register
# Register your models here.
@admin.register(savings)
class savingsAdmin(admin.ModelAdmin):
    pass

@admin.register(user_register)
class user_registerAdmin(admin.ModelAdmin):
    pass