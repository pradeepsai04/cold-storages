from django.contrib import admin
from .models import dest,house,user_record
# Register your models here.
admin.site.register(dest)
admin.site.register(house)
admin.site.register(user_record)