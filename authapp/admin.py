from authapp.models import Contact
from django.contrib import admin

class ContactAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "phonenumber"]
    list_filter = ["name", "email", "phonenumber"]

admin.site.register(Contact, ContactAdmin)
