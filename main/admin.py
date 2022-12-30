from django.contrib import admin

from main.models import Finance


class FinanceAdmin(admin.ModelAdmin):
    ...

admin.site.register(Finance, FinanceAdmin)