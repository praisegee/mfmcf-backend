from django.contrib import admin

from . import models as m


@admin.register(m.BirthdayCelebrant)
class BirthdayCelebAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(m.SpotLight)
class BirthdayCelebAdmin(admin.ModelAdmin):
    list_display = ("name",)
