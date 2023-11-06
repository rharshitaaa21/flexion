from authapp.models import Contact, MembershipPlan, Enrollment, Trainer
from django.contrib import admin

class ContactAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "phonenumber"]
    list_filter = ["name", "email", "phonenumber"]



class MembershipPlanAdmin(admin.ModelAdmin):
    list_display=["plan", "price"]

class EnrollmentAdmin(admin.ModelAdmin):
    list_display=["FullName", "Email","PhoneNumber","SelectMembershipplan","SelectTrainer"]

class TrainerAdmin(admin.ModelAdmin):
    list_display=["name", "phone", "salary", "joiningDate"]


admin.site.register(Contact, ContactAdmin)
admin.site.register(Enrollment, EnrollmentAdmin)
admin.site.register(Trainer, TrainerAdmin)
admin.site.register(MembershipPlan, MembershipPlanAdmin)