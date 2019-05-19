from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class ScheduleList(models.Model):
    user_id = models.IntegerField(default=170)
    food_name = models.CharField(max_length=170)
    DateTaker = models.DateField(blank=True, null=True)
    TimeTaker = models.TimeField(blank=True, null=True)


def __self__(self):
    return self.food_name

class FoodDetails(models.Model):
    details = RichTextUploadingField(blank=True, null=True)
    gender = models.CharField(max_length=10)
    age = models.CharField(max_length=20)
    file = models.FileField(blank=True, null=True)


def __self__(self):
    return self.details

class Events(models.Model):
    event_id = models.AutoField(primary_key=True)
    exchange_id = models.CharField(max_length=255,null=True,blank=True)
    event_start = models.DateTimeField(null=True,blank=True)
    event_end = models.DateTimeField(null=True,blank=True)
    event_subject = models.CharField(max_length=255,null=True,blank=True)
    event_location = models.CharField(max_length=255,null=True,blank=True)
    event_category = models.CharField(max_length=255,null=True,blank=True)
    event_attendees = models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.event_subject

