from django.shortcuts import get_object_or_404
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView, Response

from users.serializers import ComputerSerializer

from .models import Computer


class RetrieveComputerView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, computer_id):
        computer = get_object_or_404(Computer, id=computer_id)

        serializer = ComputerSerializer(computer)

        return Response(serializer.data)
