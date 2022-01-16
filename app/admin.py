from django.contrib import admin
from app.models import medicine, patient, receipt,notes,receiptHistory,medicineoutsideHistory,blooddonation,doctorsdetails,criticalpatient
# Register your models here.

admin.site.register(patient)

admin.site.register(medicine)


admin.site.register(receipt)

admin.site.register(notes)


admin.site.register(receiptHistory)

admin.site.register(medicineoutsideHistory)

admin.site.register(blooddonation)

admin.site.register(doctorsdetails)


admin.site.register(criticalpatient)






