from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from performance_records.models import PerformanceRecord, FirmwareVersion, FusionResource
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, get_list_or_404
import json

debug_data = ""


def index(request):
    """
    Generates the chart data for index page.
    """

    # Latest Asynchronous GET Records Chart
    latest_sync_get_chart = gen_performance_resource_chart_sync('latest-sync-get-chart', get_resource_ids(action="get", exclude_resource=["fc network", "ethernet network"]), False)

    # Latest Asynchronous POST Records Chart
    latest_sync_post_chart = gen_performance_resource_chart_sync('latest-sync-post-chart', get_resource_ids(action="post", exclude_resource=["fc network", "ethernet network"]), False)

    # Latest Synchronous POST Records Chart
    latest_async_post_chart = gen_performance_resource_chart_sync('latest-async-post-chart', get_resource_ids(action="post", exclude_resource=["fc network", "ethernet network"]), True)

    context = {'latest_sync_get_chart': latest_sync_get_chart,
               'latest_sync_post_chart': latest_sync_post_chart,
               'latest_async_post_chart': latest_async_post_chart}
    return render(request, 'performance_dashboard/index.html', context)

# def trends(request):
#     fc_networks_chart       = gen_performance_resource_chart_sync('fc-networks-chart', get_resource_ids(resource="fc network"))
#     ethernet_networks_chart = gen_performance_resource_chart_sync('ethernet-networks-chart', get_resource_ids(resource="ethernet network"))
#     lig_chart               = gen_performance_resource_chart_sync('lig-chart', get_resource_ids(resource="lig"))
#     enclosure_chart         = gen_performance_resource_chart_sync_async('enclosure-chart', get_resource_ids(resource="enclosure"))
#     enclosure_grp_chart     = gen_performance_resource_chart_sync('enclosure-grp-chart', get_resource_ids(resource="enclosure group"))

#     context = {'fc_networks_chart': fc_networks_chart,
#                'ethernet_networks_chart': ethernet_networks_chart,
#                'lig_chart': lig_chart,
#                'enclosure_chart': enclosure_chart,
#                'enclosure_grp_chart': enclosure_grp_chart}
#     return render(request, 'performance_dashboard/trends.html', context)


def performance_enclosure_trends(request):
    async_enclosure_chart = gen_performance_resource_chart_sync('async-enclosure-chart', get_resource_ids(resource="enclosure"), True)
    sync_enclosure_chart = gen_performance_resource_chart_sync('sync-enclosure-chart', get_resource_ids(resource="enclosure"), False)
    context = {'sync_enclosure_chart': sync_enclosure_chart,
               'async_enclosure_chart': async_enclosure_chart}
    return render(request, 'performance_dashboard/enclosure_trends.html', context)


def performance_enclosure_group_trends(request):
    enclosure_group_chart = gen_performance_resource_chart_sync_async('enclosure-groups-chart', get_resource_ids(resource="enclosure group"))
    context = {'enclosure_group_chart': enclosure_group_chart}
    return render(request, 'performance_dashboard/enclosure_group_trends.html', context)


def performance_network_trends(request):
    fc_network_chart = gen_performance_resource_chart_sync_async('fc-network-chart', get_resource_ids(resource="fc network"))
    ethernet_network_chart = gen_performance_resource_chart_sync_async('ethernet-network-chart', get_resource_ids(resource="ethernet network"))
    context = {'fc_network_chart': fc_network_chart,
               'ethernet_network_chart': ethernet_network_chart}
    return render(request, 'performance_dashboard/network_trends.html', context)


def performance_lig_trends(request):
    lig_chart = gen_performance_resource_chart_sync_async('lig-chart', get_resource_ids(resource="lig"))
    context = {'lig_chart': lig_chart}
    return render(request, 'performance_dashboard/lig_trends.html', context)


def performance_record_data(request, id):
    record = PerformanceRecord.objects.filter(id=id)
    return render(request, 'performance_dashboard/detail.html', {'record': record})


def performance_record_tables(request):
    records = PerformanceRecord.objects.all()
    return render(request, 'performance_dashboard/records_table.html', {'records': records})


def performance_resource_tables(request):
    resources = FusionResource.objects.all()
    return render(request, 'performance_dashboard/resource_table.html', {'resources': resources})


def performance_firmware_tables(request):
    firmware = FirmwareVersion.objects.all()
    return render(request, 'performance_dashboard/firmware_table.html', {'firmware': firmware})


def performance_profile_trends(request):
    profiles_none_chart = gen_performance_resource_chart_sync_async('profiles-none-chart', get_resource_ids(resource="server profile", condition="None"))
    profiles_connections_only_chart = gen_performance_resource_chart_sync_async('profiles-connections-only-chart', get_resource_ids(resource="server profile", condition="connections_only"))
    profiles_gen8_connections_only_chart = gen_performance_resource_chart_sync_async('profiles-gen8-connections-only-chart', get_resource_ids(resource="server profile", condition="gen8_connections_only"))
    profiles_connectionless_chart = gen_performance_resource_chart_sync_async('profiles-connectionless-chart', get_resource_ids(resource="server profile", condition="connectionless"))
    profiles_firmware_chart = gen_performance_resource_chart_sync_async('profiles-firmware-chart', get_resource_ids(resource="server profile", condition="firmware"))
    profiles_everything_chart = gen_performance_resource_chart_sync_async('profiles-everything-chart', get_resource_ids(resource="server profile", condition="everything"))

    context = {'profiles_none_chart': profiles_none_chart,
               'profiles_connections_only_chart': profiles_connections_only_chart,
               'profiles_gen8_connections_only_chart': profiles_gen8_connections_only_chart,
               'profiles_connectionless_chart': profiles_connectionless_chart,
               'profiles_firmware_chart': profiles_firmware_chart,
               'profiles_everything_chart': profiles_everything_chart}
    return render(request, 'performance_dashboard/profile_trends.html', context)

# ===================================================
# DB Access
# ===================================================


def get_resource_ids(resource=None, action=None, condition=None, exclude_resource=None):

    resources = FusionResource.objects.all()

    if (resource is not None):
        resources = resources.filter(resource=resource)

    if (action is not None):
        resources = resources.filter(action=action)

    if (condition is not None):
        resources = resources.filter(condition=condition)

    ids = []
    for record in resources:
        if((exclude_resource is not None) and (record.resource in exclude_resource)):
            continue
        ids.append(record.id)

    return ids

# ===================================================
# Generate Charts
# ===================================================

# def gen_performance_resource_chart(resource_ids, title):
#   data, labels, ykeys = ([], [], [])
#   for resource_id in resource_ids:
#     data, labels, ykeys = gen_chart_data(resource_id, data, labels, ykeys)
#   return create_chart(data, labels, ykeys, title)


def gen_performance_resource_chart_sync(title, resource_ids, is_asynchronous=None, fw_version_id=None):
    data, labels, ykeys = ([], [], [])
    for resource_id in resource_ids:
        data, labels, ykeys = gen_chart_data_sync(resource_id, is_asynchronous, fw_version_id, data, labels, ykeys)
    return create_chart(data, labels, ykeys, title)


def gen_performance_resource_chart_sync_async_fw(title, resource_ids):
    data, labels, ykeys = ([], [], [])
    for resource_id in resource_ids:
        data, labels, ykeys = gen_chart_data_sync(resource_id, True, fw_version_id, data, labels, ykeys)
        data, labels, ykeys = gen_chart_data_sync(resource_id, False, fw_version_id, data, labels, ykeys)
    return create_chart(data, labels, ykeys, title)


def gen_performance_resource_chart_sync_async(title, resource_ids, fw_version_id=None):
    data, labels, ykeys = ([], [], [])
    for resource_id in resource_ids:
        data, labels, ykeys = gen_chart_data_sync(resource_id, True, fw_version_id, data, labels, ykeys)
        data, labels, ykeys = gen_chart_data_sync(resource_id, False, fw_version_id, data, labels, ykeys)
    return create_chart(data, labels, ykeys, title)

# ===================================================
# Chart Utility Functions
# ===================================================

# def gen_chart_data(resource_id, data=[], labels=[], ykeys=[]):
#  try:
#    records = PerformanceRecord.objects.filter(resource_id=resource_id)
#  except PerformanceRecord.DoesNotExist:
#    return data, labels, ykeys
#  if len(records)==0:
#    return data, labels, ykeys
#  labels.append(str(records[0].resource_id.action) + " " + str(records[0].resource_id.resource))
#  key = str(len(labels))
#  ykeys.append(key)
#  i = 1
#  for record in records:
#    dict = {'y': i, key: int(record.duration)}
#    data.append(dict)
#    i += 1
#  return data, labels, ykeys


def gen_chart_data_sync(resource_id, is_asynchronous, fw_version_id, data=[], labels=[], ykeys=[]):
    label = ""

    try:
        records = PerformanceRecord.objects.filter(resource_id=resource_id)
        label = str(records[0].resource_id.action) + " " + str(records[0].resource_id.resource) + " " + str(records[0].resource_id.condition)
    except PerformanceRecord.DoesNotExist:
        return data, labels, ykeys
    except IndexError:
        return data, labels, ykeys

    if (is_asynchronous is not None):
        records = records.filter(is_asynchronous=is_asynchronous)
        label = "Asynchronous " + label if is_asynchronous else "synchronous " + label

    if (fw_version_id is not None):
        records = records.filter(fw_version_id=fw_version_id)
        label += "(" + str(records[0].resource_id.fusion_release) + ")"

    # labels.append(label + str(records[0].resource_id.action) + " " + str(records[0].resource_id.resource))
    if len(records) == 0:
        return data, labels, ykeys

    labels.append(label)
    key = str(len(labels))
    ykeys.append(key)
    i = 0
    for record in records:
        try:
            dict = data[i]
            dict[key] = int(record.duration)
            data[i] = dict
        except IndexError:
            dict = {'y': i + 1}
            dict[key] = int(record.duration)
            data.append(dict)
        i += 1
    return data, labels, ykeys


def create_chart(data, labels, ykeys, title):
    # TODO: Add Synchronous and asynchronous goals to charts
    config = {
        'data': data,
        'xkey': 'y',
        'ykeys': ykeys,
        'labels': labels,
        'fillOpacity': 0.6,
        'parseTime': 'false',
        # 'xLabelFormat': 'function(x) { return x.toString()[-2]; }',
        'hideHover': 'auto',
        'behaveLikeLine': 'false',
        'resize': 'true',
        'pointFillColors': ['#ffffff'],
        'pointStrokeColors': ['black'],
        'lineColors': ['gray', 'red', 'blue', 'green', 'orange'],
        'element': title
    }
    return config
