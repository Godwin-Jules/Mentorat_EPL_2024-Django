from django.db import models
from datetime import datetime
from django.utils.text import slugify


# Create your models here.

months_list_en = [
    ("jan", "January"),
    ("feb", "February"),
    ("mar", "March"),
    ("apr", "April"),
    ("may", "May"),
    ("jun", "June"),
    ("jul", "July"),
    ("aug", "August"),
    ("sep", "September"),
    ("oct", "October"),
    ("nov", "November"),
    ("dec", "December"),
]

# def get_month():
#     month_id = datetime.today().month
#     month_str = months_list_en[month_id - 1][0]
#     current_month = Month.objects.get(month=month_str)
#     return current_month


class Month(models.Model):
    month = models.CharField(max_length=3, choices=months_list_en, unique=True)

    def __str__(self):
        return self.month


class Goal(models.Model):
    label = models.CharField(max_length=120, unique=True, blank=False, null=False)

    def __str__(self):
        return self.label


class Skill(models.Model):
    title = models.CharField(max_length=25, unique=True, blank=False, null=False)
    description = models.CharField(max_length=100, default="", blank=True)
    slug = models.SlugField()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class Challenge(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True, db_index=True)
    date = models.DateField(auto_now=True, blank=False, null=False)
    month = models.ManyToManyField(Month, related_name="challenges")
    skills = models.ManyToManyField(Skill, blank=True, default=None, related_name="challenges")
    goals = models.ManyToManyField(Goal, blank=True, default=None, related_name="challenges")
    content = models.TextField(max_length=1500, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)