from django.contrib import admin
from .models import Assigned, addAssigned, addBillable


class assignitemAdmin(admin.ModelAdmin):
    list_display = ('detail_id','assign_date')
class addassignitemAdmin(admin.ModelAdmin):
    list_display = ('user','resource','assigned')



admin.site.register(Assigned,assignitemAdmin)
admin.site.register(addAssigned,addassignitemAdmin)
admin.site.register(addBillable)