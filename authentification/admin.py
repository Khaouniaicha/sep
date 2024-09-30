from django.contrib import admin
from .models import Alert

@admin.register(Alert)
class AlertAdmin(admin.ModelAdmin):
    list_display = ('alert_type', 'user', 'address', 'created_at')
    search_fields = ('alert_type', 'user__username', 'address')
    list_filter = ('alert_type', 'created_at')
    readonly_fields = ('created_at', 'user')  # Make 'user' read-only in the admin

    def save_model(self, request, obj, form, change):
        if not obj.pk:  # If this is a new alert
            obj.user = request.user  # Automatically assign the logged-in user (superuser)
        super().save_model(request, obj, form, change)
