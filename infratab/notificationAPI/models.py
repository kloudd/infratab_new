from django.db import models
from datetime import datetime
# Create your models here.

DAYS_OF_WEEK = (
('1', 'Monday'),
('2', 'Tuesday'),
('3', 'Wednesday'),
('4', 'Thursday'),
('5', 'Friday'),
('6', 'Saturday'),
('7', 'Sunday'),
)

class Days(models.Model):
    days = models.CharField(max_length=1, choices=DAYS_OF_WEEK)


class Notification(models.Model):

    phone_no = models.IntegerField(blank=True, default='')
    email = models.CharField(max_length=100, blank=True, default='')

    date = models.DateTimeField(default=datetime.now,blank=True)
    is_recurring = models.BooleanField(default=True)
    # notification = models.ForeignKey(Notification, related_name='recurring_notifications')

    last_date = models.DateTimeField(default=datetime.now,blank=True)
    is_week_day = models.BooleanField(default=True)
    days = models.ManyToManyField(Days, blank=True)


# class RecurringNotifications(models.Model):


