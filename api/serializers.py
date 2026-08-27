from rest_framework import serializers
from person.models import Person
from student.models import Students
from car.models import Car


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model=Car
        fields='__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Students
        fields='__all__'


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model=Person
        fields='__all__'