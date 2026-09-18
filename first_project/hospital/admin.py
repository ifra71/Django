from django.contrib import admin

from .models import Doctor, Hospital, MedicalRecord, Nurse, Patient

admin.site.register(Doctor)
admin.site.register(Nurse)
admin.site.register(Patient)
admin.site.register(Hospital)
admin.site.register(MedicalRecord)
