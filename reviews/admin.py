from django.contrib import admin

from .models import Position,Review
admin.site.register(Position)
admin.site.register(Review)


class PositionAdmin(admin.ModelAdmin):
    fields = ('company_name', 'jobtitle', 'location')
    list_fields = ('company_name', 'jobtitle', 'location')