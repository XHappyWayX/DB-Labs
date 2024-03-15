from rest_framework.views import APIView
from .models import Resource
from rest_framework.response import Response
from django.http import JsonResponse
from .serializers import ResourcesSerializer


class GetData(APIView):
    def get(self, request, *args, **kwargs):
        resource_id = request.query_params.get('id')
        resource_name = request.query_params.get('name')
        in_stock = request.query_params.get('in_stock')
        spent_per_month = request.query_params.get('spent_per_month')
        spent_in_total = request.query_params.get('spent_in_total')

        queryset = Resource.objects.all()

        if resource_id:
            queryset = queryset.filter(id__icontains=resource_id)

        if in_stock:
            queryset = queryset.filter(in_stock=in_stock)
        if spent_per_month:
            queryset = queryset.filter(spent_per_month=spent_per_month)
        if spent_in_total:
            queryset = queryset.filter(spent_in_total=spent_in_total)

        if resource_name:
            queryset = queryset.filter(name=resource_name)

        serializer = ResourcesSerializer(queryset, many=True)
        return Response(serializer.data)