from rest_framework import serializers
from .models import Component, Vehicle, Repair

class ComponentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Component
        fields = '__all__'

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'

class RepairSerializer(serializers.ModelSerializer):
    total_cost = serializers.SerializerMethodField()

    class Meta:
        model = Repair
        fields = '__all__'

    def get_total_cost(self, obj):
        return obj.total_cost()
