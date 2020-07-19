from django.contrib import admin
from .models import Update
from django.db import models
from tinymce.widgets import TinyMCE


class UpdateAdmin(admin.ModelAdmin):

    fieldsets = [
        ("Title/Date", {"fields": ["update_title"]}),
        ("Content", {"fields": ["update_content", "update_username"]}),
    ]

    formfield_overrides = {
        models.TextField: {"widget": TinyMCE()}
    }


admin.site.register(Update, UpdateAdmin)
