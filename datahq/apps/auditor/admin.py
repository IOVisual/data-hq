from django.contrib import admin
from auditor.models import * 
from django.contrib.auth.models import User


class AuditEventAdmin(admin.ModelAdmin):
    list_display = ('id','user','event_class','description', 'event_date')
    list_filter = ['user','event_class','description']
    
admin.site.register(AuditEvent, AuditEventAdmin)  
