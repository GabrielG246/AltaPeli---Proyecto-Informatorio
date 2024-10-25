from django.contrib import admin
from .models import User








class UserAdmin(admin.ModelAdmin):
       list_display = ('nombre',)
       search_fields = ('usuario')
       list_filter = ('usuario', 'email')

admin.site.register(User)