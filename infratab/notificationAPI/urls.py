from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [

    url(r'^index', views.index, name='index'),

    url(r'^notification/$', views.NotificationList.as_view()),
    url(r'^notification/(?P<pk>[0-9]+)/$', views.NotificationDetail.as_view()),

    # url(r'^recurring_notification/$', views.NotificationList.as_view()),
    # url(r'^recurring_notification/(?P<pk>[0-9]+)/$', views.NotificationDetail.as_view()),
    #
    # url(r'^days_notification/$', views.NotificationList.as_view()),
    # url(r'^days_notification/(?P<pk>[0-9]+)/$', views.NotificationDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)