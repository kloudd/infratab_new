from rest_framework import serializers
from .models import Days, Notification\
    # , RecurringNotifications


# class NotificationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Notification
#         fields = ('phone_no', 'email', 'date', 'is_recurring')
#
#
#
# class RecurringNotificationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = RecurringNotifications
#         fields = ('notification', 'last_date', 'is_week_day', 'is_some_days')
#
#
#
# class DaysNotificationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Days
#         fields = ('recurringNotification', 'days')


class NotificationSerializer(serializers.ModelSerializer):
    # recurring_notifications = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # recurring_notification_is_week_day= serializers.BooleanField(source='recurringNotifications.is_week_day')
    # recurring_notification_days = serializers.RelatedField(source='recurringNotifications.days.days')


    class Meta:
        model = Notification
        fields = ('id','phone_no', 'email', 'date', 'is_recurring', 'last_date', 'is_week_day', 'days')