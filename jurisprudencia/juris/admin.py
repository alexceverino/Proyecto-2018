from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import *

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class perfilInline(admin.StackedInline):
    model = perfil
    can_delete = False
    verbose_name_plural = 'perfil'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (perfilInline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

class LogAdminSenten(admin.ModelAdmin):
    list_display = ["__str__","fecha_agregacion"]

    list_filter = ["fecha_agregacion"]
    search_fields = ["rut","nombre","fecha_agregacion"]
    class Meta:
        model = sentencia

#admin.site.register(usuario,LogAdminUser)
admin.site.register(sentencia,LogAdminSenten)
admin.site.register(tribunal)
