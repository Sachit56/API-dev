from django.contrib import admin
from .models import *
# Register your models here.


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_staff','age')

admin.site.register(CustomUser,CustomUserAdmin)
admin.site.register(WheelSpecificationForm)
admin.site.register(BogieForm)
admin.site.register(WheelSpecification)
admin.site.register(BoggieDetails)
admin.site.register(BogieCheckSheet)
admin.site.register(BmbcChecksheet)