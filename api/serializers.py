from rest_framework import serializers
from person.models import Person
from student.models import Students
from car.models import Car
from house.models import House
from employee.models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields='__all__'
class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model=House
        fields='__all__'
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