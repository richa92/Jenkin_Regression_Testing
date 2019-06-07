from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from performance_records.models import PerformanceRecord, FirmwareVersion, FusionResource
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, get_list_or_404, render_to_response
import json

debug_data = ""


def index(request):
    """
    Generates the chart data for index page. This page will contain the 'most useful' charts.
    """
    charts = []

    # Add Server Profile Chart
    resource_name = "server profile"
    fw_id = "1"
    condition = None

    results = FirmwareVersion.objects.filter(id=fw_id)
    chart_name = "%s with a %s condition on %s %s (%s)" % (resource_name.title(), condition, results[0].platform, results[0].fusion_release, results[0].feature_set)
    chart_id = '%s-chart-%s-%s' % (resource_name.replace(" ", "-").lower(), str(fw_id), str(condition).lower)

    # Generate chart
    chart = {'name': chart_name, 'id': chart_id}
    data, labels, ykeys = add_data_to_chart("get", resource_name, [], [], [], fw_version_id=fw_id, condition=condition)
    data, labels, ykeys = add_data_to_chart("post", resource_name, data, labels, ykeys, fw_version_id=fw_id, condition=condition, is_asynchronous=True)
    data, labels, ykeys = add_data_to_chart("post", resource_name, data, labels, ykeys, fw_version_id=fw_id, condition=condition, is_asynchronous=False)
    data, labels, ykeys = add_data_to_chart("delete", resource_name, data, labels, ykeys, fw_version_id=fw_id, condition=condition)
    data, labels, ykeys = add_data_to_chart("login", resource_name, data, labels, ykeys, fw_version_id=fw_id, condition=condition)
    chart['data'] = create_chart(data, labels, ykeys, chart_id)
    charts.append(chart)

    # Add Logical Enclosure Chart
    resource_name = "logical enclosure"
    fw_id = "1"
    condition = None

    results = FirmwareVersion.objects.filter(id=fw_id)
    chart_name = "%s with a %s condition on %s %s (%s)" % (resource_name.title(), condition, results[0].platform, results[0].fusion_release, results[0].feature_set)
    chart_id = '%s-chart-%s-%s' % (resource_name.replace(" ", "-").lower(), str(fw_id), str(condition).lower)

    # Generate chart
    chart = {'name': chart_name, 'id': chart_id}
    data, labels, ykeys = add_data_to_chart("get", resource_name, [], [], [], fw_version_id=fw_id, condition=condition)
    data, labels, ykeys = add_data_to_chart("post", resource_name, data, labels, ykeys, fw_version_id=fw_id, condition=condition, is_asynchronous=True)
    data, labels, ykeys = add_data_to_chart("post", resource_name, data, labels, ykeys, fw_version_id=fw_id, condition=condition, is_asynchronous=False)
    data, labels, ykeys = add_data_to_chart("delete", resource_name, data, labels, ykeys, fw_version_id=fw_id, condition=condition)
    data, labels, ykeys = add_data_to_chart("login", resource_name, data, labels, ykeys, fw_version_id=fw_id, condition=condition)
    chart['data'] = create_chart(data, labels, ykeys, chart_id)
    charts.append(chart)

    # Add LIG Chart
    resource_name = "lig"
    fw_id = "1"
    condition = None

    results = FirmwareVersion.objects.filter(id=fw_id)
    chart_name = "%s with a %s condition on %s %s (%s)" % (resource_name.title(), condition, results[0].platform, results[0].fusion_release, results[0].feature_set)
    chart_id = '%s-chart-%s-%s' % (resource_name.replace(" ", "-").lower(), str(fw_id), str(condition).lower)

    # Generate chart
    chart = {'name': chart_name, 'id': chart_id}
    data, labels, ykeys = add_data_to_chart("get", resource_name, [], [], [], fw_version_id=fw_id, condition=condition)
    data, labels, ykeys = add_data_to_chart("post", resource_name, data, labels, ykeys, fw_version_id=fw_id, condition=condition, is_asynchronous=True)
    data, labels, ykeys = add_data_to_chart("post", resource_name, data, labels, ykeys, fw_version_id=fw_id, condition=condition, is_asynchronous=False)
    data, labels, ykeys = add_data_to_chart("delete", resource_name, data, labels, ykeys, fw_version_id=fw_id, condition=condition)
    data, labels, ykeys = add_data_to_chart("login", resource_name, data, labels, ykeys, fw_version_id=fw_id, condition=condition)
    chart['data'] = create_chart(data, labels, ykeys, chart_id)
    charts.append(chart)

    # Add Data to Chart for HTML Display
    context = {'charts': charts}
    return render(request, 'performance_dashboard/index.html', context)

# ===================================================
# Trend Chart Pages
# ===================================================


def performance_enclosure_trends(request):
    # Build Chart Data
    resource_name = "enclosure"
    eg_charts = add_all_charts(resource_name.lower())

    # Add Data to Chart for HTML Display
    context = {'title': resource_name.title(),
               'charts': eg_charts}
    return render(request, 'performance_dashboard/trends.html', context)


def performance_enclosure_group_trends(request):
    # Build Chart Data
    resource_name = "enclosure group"
    eg_charts = add_all_charts(resource_name.lower())

    # Add Data to Chart for HTML Display
    context = {'title': resource_name.title(),
               'charts': eg_charts}
    return render(request, 'performance_dashboard/trends.html', context)


def performance_lig_trends(request):
    # Build Chart Data
    resource_name = "lig"

    # Add Data to Chart for HTML Display
    charts = add_all_charts(resource_name.lower())
    context = {'title': "Logical Interconnect Group",
               'charts': charts}
    return render(request, 'performance_dashboard/trends.html', context)


def performance_appliance_trends(request):
    # Build Chart Data
    resource_name = "appliance"

    # Add Data to Chart for HTML Display
    charts = add_all_charts(resource_name.lower())
    context = {'title': resource_name.title(),
               'charts': charts}
    return render(request, 'performance_dashboard/trends.html', context)


def performance_ethernet_network_trends(request):
    # Build Chart Data
    resource_name = "ethernet network"

    # Add Data to Chart for HTML Display
    charts = add_all_charts(resource_name.lower())
    context = {'title': resource_name.title(),
               'charts': charts}
    return render(request, 'performance_dashboard/trends.html', context)


def performance_fc_network_trends(request):
    # Build Chart Data
    resource_name = "fc network"

    # Add Data to Chart for HTML Display
    charts = add_all_charts(resource_name.lower())
    context = {'title': resource_name.title(),
               'charts': charts}
    return render(request, 'performance_dashboard/trends.html', context)


def performance_interconnect_trends(request):
    # Build Chart Data
    resource_name = "interconnect"

    # Add Data to Chart for HTML Display
    charts = add_all_charts(resource_name.lower())
    context = {'title': resource_name.title(),
               'charts': charts}
    return render(request, 'performance_dashboard/trends.html', context)


def performance_logical_enclosure_trends(request):
    # Build Chart Data
    resource_name = "logical enclosure"

    # Add Data to Chart for HTML Display
    charts = add_all_charts(resource_name.lower())
    context = {'title': resource_name.title(),
               'charts': charts}
    return render(request, 'performance_dashboard/trends.html', context)


def performance_server_hardware_trends(request):
    # Build Chart Data
    resource_name = "server hardware"

    # Add Data to Chart for HTML Display
    charts = add_all_charts(resource_name.lower())
    context = {'title': resource_name.title(),
               'charts': charts}
    return render(request, 'performance_dashboard/trends.html', context)


def performance_profile_trends(request):
    # Build Chart Data
    resource_name = "server profile"

    # Add Data to Chart for HTML Display
    charts = add_all_charts(resource_name.lower())
    context = {'title': resource_name.title(),
               'charts': charts}
    return render(request, 'performance_dashboard/trends.html', context)


def performance_record_data(request, id):
    record = PerformanceRecord.objects.filter(id=id)
    return render(request, 'performance_dashboard/detail.html', {'record': record})

# ===================================================
# Data Table Pages
# ===================================================


def performance_record_tables(request):
    records = PerformanceRecord.objects.all()
    return render(request, 'performance_dashboard/records_table.html', {'records': records})


def performance_resource_tables(request):
    resources = FusionResource.objects.all()
    return render(request, 'performance_dashboard/resource_table.html', {'resources': resources})


def performance_firmware_tables(request):
    firmware = FirmwareVersion.objects.all()
    return render(request, 'performance_dashboard/firmware_table.html', {'firmware': firmware})


# ===================================================
# DB Access
# ===================================================

def add_all_charts(resource_name):
    # Plot lines for GET, POST, DELETE, LOGIN actions onto chart data.
    #
    # context = { 'charts': [ {'name': "Title of the chart to be displayed",
    #                          'id':   'first-chart-id',
    #                          'data': {firstChartData} },
    #                         {'name': "Second Chart Title",
    #                          'id':   'second-chart-id',
    #                          'data': {secondChartData} },
    #                       ]
    #           }
    charts = []

    # Get All EG Conditions
    conditions = get_conditions(resource_name)
    for condition in conditions:
        # Get EG Firmware Version Ids for each condition
        fw_ids = get_fw_version_ids(resource=resource_name, condition=condition)
        for fw_id in fw_ids:
            results = FirmwareVersion.objects.filter(id=fw_id)
            chart_name = "%s with a %s condition on %s %s (%s)" % (resource_name.title(), condition, results[0].platform, results[0].fusion_release, results[0].feature_set)
            chart_id = '%s-chart-%s-%s' % (resource_name.replace(" ", "-").lower(), str(fw_id), str(condition).lower)

            # Generate chart data
            chart = {'name': chart_name, 'id': chart_id}
            data, labels, ykeys = add_data_to_chart("get", resource_name, [], [], [], fw_version_id=fw_id, condition=condition)
            data, labels, ykeys = add_data_to_chart("post", resource_name, data, labels, ykeys, fw_version_id=fw_id, condition=condition, is_asynchronous=True)
            data, labels, ykeys = add_data_to_chart("post", resource_name, data, labels, ykeys, fw_version_id=fw_id, condition=condition, is_asynchronous=False)
            data, labels, ykeys = add_data_to_chart("delete", resource_name, data, labels, ykeys, fw_version_id=fw_id, condition=condition)
            data, labels, ykeys = add_data_to_chart("login", resource_name, data, labels, ykeys, fw_version_id=fw_id, condition=condition)
            chart['data'] = create_chart(data, labels, ykeys, chart_id)
            charts.append(chart)
    return charts


def get_conditions(resource, action=None):
    conditions = []
    results = FusionResource.objects.filter(resource=resource)
    if action is not None:
        results = results.filter(action=action)
    results = results.order_by().values('condition').distinct()
    for result in results:
        conditions.append(result['condition'])
    return conditions


def get_fw_version_ids(resource, action=None, condition=None):
    fw_ids = []
    resource_ids = get_resource_ids(resource=resource, action=action, condition=condition)

    for resource_id in resource_ids:
        results = PerformanceRecord.objects.filter(resource_id=resource_id).order_by().values('fw_version_id').distinct()
        for result in results:
            if result['fw_version_id'] not in fw_ids:
                fw_ids.append(result['fw_version_id'])
    return fw_ids


def add_data_to_chart(action, resource, data, labels, ykeys, label=None, condition=None, fw_version_id=None, is_asynchronous=None):
    ids = get_resource_ids(resource=resource, action=action, condition=condition)
    records = []
    for id in ids:
        tmp = PerformanceRecord.objects.filter(resource_id=id)
        if is_asynchronous is not None:
            tmp = tmp.filter(is_asynchronous=is_asynchronous)
        if fw_version_id is not None:
            tmp = tmp.filter(fw_version_id=fw_version_id)
        records.extend(tmp)
    if label is None:
        label = "%s %s" % (action.upper(), resource.title())
        # Add in asynchronous data to label if needed.
        if is_asynchronous is not None:
            label += " (Asynchronous)" if is_asynchronous else " (Synchronous)"
    return gen_chart_data(records, label, data, labels, ykeys)


def get_resource_ids(resource=None, action=None, condition=None, exclude_resource=None):

    resources = FusionResource.objects.all()

    # Filter based on FusionResource fields.
    if (resource is not None):
        resources = resources.filter(resource=resource)

    if (action is not None):
        resources = resources.filter(action=action)

    if (condition is not None):
        resources = resources.filter(condition=condition)

    ids = []
    # Filter based on PerformanceRecord fields.
    for record in resources:
        if((exclude_resource is not None) and (record.resource in exclude_resource)):
            continue
        ids.append(record.id)

    return ids

# ===================================================
# Chart Utility Functions
# ===================================================


def gen_chart_data(records, label, data=[], labels=[], ykeys=[]):
    if len(records) == 0:
        return data, labels, ykeys

    labels.append(label)
    key = str(len(labels))
    ykeys.append(key)

    # Build data from records
    for record in records:
        temp_data = {'y': str(record.time)}
        temp_data[key] = int(record.duration)
        data.append(temp_data)

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
