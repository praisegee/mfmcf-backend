from django.contrib import admin

from . import models as m


@admin.register(m.BirthdayCelebrant)
class BirthdayCelebrantAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(m.SpotLight)
class SpotLightAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(m.Executive)
class ExecutiveAdmin(admin.ModelAdmin):
    list_display = ("fullname",)
