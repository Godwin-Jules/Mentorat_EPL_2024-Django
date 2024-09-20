from django.contrib import admin
from .models import *


# Register your models here.

@admin.register(Month)
class MonthAdmin(admin.ModelAdmin):
    sortable_by = ("-id",)
    list_display = ("month",)
    list_filter = ("month",)


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("title", "slug",)
    list_filter = ("title",)
    sortable_by = ("title",)


@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    list_display = ("label",)
    list_filter = ("label",)
    sortable_by = ("label", "id")


@admin.register(Challenge)
class ChallengeAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ("name", "date",)
    list_filter = ("date", "month")
    sortable_by = ("-date", "month")
