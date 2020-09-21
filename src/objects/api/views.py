from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from objects.core.models import Object

from .serializers import HistoryRecordSerializer, ObjectSerializer


class ObjectViewSet(viewsets.ModelViewSet):
    queryset = Object.objects.order_by("-pk")
    serializer_class = ObjectSerializer
    lookup_field = "uuid"

    @swagger_auto_schema(responses={200: HistoryRecordSerializer(many=True)})
    @action(detail=True, methods=["get"], serializer_class=HistoryRecordSerializer)
    def history(self, request, uuid=None):
        records = self.get_object().records.order_by("id")
        serializer = self.get_serializer(records, many=True)
        return Response(serializer.data)