from django.contrib import admin
from .models import Applicant, Document, Details, Sport, Subject, StudyHistory, SpecialNeed, Choice


# Register your models here.


admin.site.register(Applicant)
admin.site.register(Document)
admin.site.register(Details)
admin.site.register(Sport)
admin.site.register(Subject)
admin.site.register(StudyHistory)
admin.site.register(SpecialNeed)
admin.site.register(Choice)
