from django.contrib import admin

from .models import Registration, Subject, GradeAttendance

admin.site.register(Registration)
admin.site.register(Subject)
admin.site.register(GradeAttendance)

