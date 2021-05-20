from django.contrib import admin
from .models import Post, Vote

# To show a hidden field in admin panel without ability to modify it
# Must be added to register procedure
class ShowHiddenFields(admin.ModelAdmin):
    readonly_fields = (
        'created_at',
    )

# Register your models here.
admin.site.register(Post, ShowHiddenFields)
admin.site.register(Vote, ShowHiddenFields)