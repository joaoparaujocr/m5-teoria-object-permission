from rest_framework import serializers

from .models import Computer


class ComputerSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    name = serializers.CharField(max_length=100)
    user_id = serializers.IntegerField()

    def create(self, validated_data):
        return Computer.objects.create(**validated_data)
