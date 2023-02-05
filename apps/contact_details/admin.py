from django.contrib import admin

from apps.contact_details.models import ContactAppend


@admin.register(ContactAppend)
class ContactAppendAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'contact', )
