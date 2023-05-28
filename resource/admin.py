from django.contrib import admin
from .models import Details

# Register your models here.
class  resourceAdmin(admin.ModelAdmin):
    list_display = ('name','desc','start_date','cost')
    
admin.site.register(Details,resourceAdmin)
