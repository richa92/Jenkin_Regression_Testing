from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from performance_records.models import PerformanceRecord, FirmwareVersion, FusionResource
from performance_records.serializers import PerformanceRecordSerializer, FirmwareVersionSerializer, FusionResourceSerializer
from django.http import HttpResponse
# from django.template import RequestContext, loader
from django.shortcuts import get_object_or_404, render

# @csrf_exempt


@api_view(['GET', 'POST'])
def performance_records(request, format=None):
    """
    List all performance_records, or create a new performance record.
    """
    if request.method == 'GET':
        performance_records = PerformanceRecord.objects.all()
        serializer = PerformanceRecordSerializer(performance_records, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PerformanceRecordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def performance_record_details(request, pk, format=None):
    """
    Retrieve, update or delete a performance record instance.
    """
    try:
        performance_records = PerformanceRecord.objects.get(pk=pk)
    except PerformanceRecord.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PerformanceRecordSerializer(performance_records)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PerformanceRecordSerializer(performance_records, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        performance_records.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#  Data Access Functions


def index(request):
    latest_records = PerformanceRecord.objects.order_by('id')[:5]
    context = {'latest_records': latest_records}
    return render(request, 'performance_records/index.html', context)


def performance_record_data(request, id):
    record = get_object_or_404(PerformanceRecord, id=id)
    return render(request, 'performance_records/detail.html', {'record': record})

# View Sets


class PerformanceViewSet(viewsets.ModelViewSet):

    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = PerformanceRecord.objects.all()
    serializer_class = PerformanceRecordSerializer


class FusionResourceViewSet(viewsets.ModelViewSet):

    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = FusionResource.objects.all()
    serializer_class = FusionResourceSerializer


class FirmwareVersionViewSet(viewsets.ModelViewSet):

    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = FirmwareVersion.objects.all()
    serializer_class = FirmwareVersionSerializer
