from django.contrib import admin

from apps.message.models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'chat', 'created_at',)
