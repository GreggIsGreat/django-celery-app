from django.db import models
from rest_framework import serializers
from .models import employee_database


class employee_databaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = employee_database
        fields = '__all__'
