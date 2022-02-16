from django.contrib import admin
from liffapp.models import *


class cpuAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'commodity',
                    'vendor')
    list_filter = ('name', 'price')
    search_fields = ('name',)
    ordering = ('id',)
# Register your models here.
