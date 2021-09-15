from django.contrib import admin

from .models import FeedBack

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'description')

admin.site.register(FeedBack, FeedbackAdmin)
