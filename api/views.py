from django.shortcuts import render
from person.models import Person
from student.models import Students
from car.models import Car
from .serializers import PersonSerializer,StudentSerializer,CarSerializer
from rest_framework.response import Response
from rest_framework import status 
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import mixins,generics
from django.http import Http404

# Create your views here.


#Function Based Rest API
@api_view(['GET','POST'])
def person (request):
    if(request.method=='GET'):
        personObj=Person.objects.all()
        serializedPerson=PersonSerializer(personObj,many=True)
        return Response(serializedPerson.data,status=200)

    elif request.method=='POST':
        addData=PersonSerializer(data=request.data)
        if addData.is_valid():
            addData.save()
            return Response(addData.data,status=200)
        else:
            return Response(addData.errors,status=400)

@api_view(['GET','PUT','DELETE'])
def getPerson(request,id):
    try:
        obj=Person.objects.get(id=id)
       
    except Person.DoesNotExist:
        return Http404
    
    if request.method=='GET':
        peronObj= PersonSerializer(obj)
        return Response(peronObj.data,status=200)
    
    elif request.method=='PUT':
        personObj=PersonSerializer(obj,data=request.data)
        if personObj.is_valid():
            personObj.save()
            return Response(personObj.data,status=200)
        else:
            return Response(peronObj.errors,status=400)

    elif request.method=='DELETE':
        obj.delete()
        return Response(status=200)

#Class Based REST API
class Student(APIView):
    def get(self,request):
        person=Students.objects.all()
        ser=StudentSerializer(person,many=True)
        return Response(ser.data,status=200)

    def post(self,request):
        ser=StudentSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data,status=200)
        else:
            return Response(ser.errors,status=400)

class StudentDetails(APIView):

    def getDetails(self,id):
        try:
            student=Students.objects.get(id=id)
            return student
        except Student.DoesNotExist:
            return Http404

    def get(self,request,id):
        obj=self.getDetails(id)
        ser=StudentSerializer(obj)
        return Response(ser.data,status=200)
        
    def put(self,request,id):
        obj=self.getDetails(id)
        ser=StudentSerializer(obj,data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data,status=200)
        else:
            return Response(ser.errors,status=400)

    def delete(self,request,id):
            obj=self.getDetails(id)
            obj.delete()
            return Response(status=200)


#Mixins#
class Cars(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset=Car.objects.all()
    serializer_class=CarSerializer
    def get(self,request):
        return self.list(request)

    def post(self,request):
        return self.create(request)

class CarDetail(mixins.RetrieveModelMixin,mixins.DestroyModelMixin,mixins.UpdateModelMixin,generics.GenericAPIView):
    queryset=Car.objects.all()
    serializer_class=CarSerializer
    lookup_field='id'
    def get(self,request,id):
        return self.retrieve(request,pk=id)
    def put(self,requset,id):
        return self.update(requset,pk=id)
    def delete(self,requset,id):
        return self.destroy(requset,pk=id)

