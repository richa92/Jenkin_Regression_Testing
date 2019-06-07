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
    url(r'^appliance_trends/$', views.performance_appliance_trends, name='appliance_trends'),
    url(r'^enclosure_trends/$', views.performance_enclosure_trends, name='enclosure_trends'),
    url(r'^profile_trends/$', views.performance_profile_trends, name='profile_trends'),
    url(r'^enclosure_trends/$', views.performance_enclosure_trends, name='enclosure_trends'),
    url(r'^enclosure_group_trends/$', views.performance_enclosure_group_trends, name='enclosure_group_trends'),
    # url(r'^network_trends/$', views.performance_network_trends, name='network_trends'),
    url(r'^ethernet_network_trends/$', views.performance_ethernet_network_trends, name='ethernet_network_trends'),
    url(r'^fc_network_trends/$', views.performance_fc_network_trends, name='fc_network_trends'),
    url(r'^interconnect_trends/$', views.performance_interconnect_trends, name='interconnect_trends'),
    url(r'^logical_enclosure_trends/$', views.performance_logical_enclosure_trends, name='logical_enclosure_trends'),
    url(r'^server_hardware_trends/$', views.performance_server_hardware_trends, name='server_hardware_trends'),
    url(r'^lig_trends/$', views.performance_lig_trends, name='lig_trends'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
