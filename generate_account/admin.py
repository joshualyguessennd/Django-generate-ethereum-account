from django.contrib import admin
from .models import Generated_adress
# Register your models here.

class GenerateAddress(admin.ModelAdmin):
    list_display = ['id','address', 'value', 'user_id']
    search_fields = ['id',]

admin.site.register(Generated_adress, GenerateAddress)