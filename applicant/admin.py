from django.contrib import admin
from .models import Personal, NextOfKin, Fees, SouthAfricanQualifications, InternationalQualifications

# Register your models here.

admin.site.register(Personal)
admin.site.register(NextOfKin)
admin.site.register(Fees)
admin.site.register(SouthAfricanQualifications)
admin.site.register(InternationalQualifications)
