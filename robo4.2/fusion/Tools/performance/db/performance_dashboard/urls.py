from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from performance_dashboard import views

app_name = 'performance_dashboard'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<id>[0-9]+)/$', views.performance_record_data, name='details'),
    # url(r'^trends/$', views.trends, name='trends'),
    url(r'^records_tables/$', views.performance_record_tables, name='records_tables'),
    url(r'^resource_tables/$', views.performance_resource_tables, name='resource_tables'),
    url(r'^firmware_tables/$', views.performance_firmware_tables, name='firmware_tables'),
    url(r'^profile_trends/$', views.performance_profile_trends, name='profile_trends'),
    url(r'^enclosure_trends/$', views.performance_enclosure_trends, name='enclosure_trends'),
    url(r'^enclosure_group_trends/$', views.performance_enclosure_group_trends, name='enclosure_group_trends'),
    url(r'^network_trends/$', views.performance_network_trends, name='network_trends'),
    url(r'^lig_trends/$', views.performance_lig_trends, name='lig_trends'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
