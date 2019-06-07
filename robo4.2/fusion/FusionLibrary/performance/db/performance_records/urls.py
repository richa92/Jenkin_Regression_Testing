from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from performance_records import views

app_name = 'performance_records'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<id>[0-9]+)/$', views.performance_record_data, name='details'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
