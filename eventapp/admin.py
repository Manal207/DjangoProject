from django.contrib import admin
from .models import Event

# Optional: To customize how your model appears in the admin interface
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'location', 'participants')  # Fields to display in the model list page
    search_fields = ('name', 'location')  # Fields to be searched in the admin list page
    list_filter = ('date',)  # Fields to filter by in the sidebar
    ordering = ('date',)  # Default ordering

# Register your models here.
admin.site.register(Event, EventAdmin)