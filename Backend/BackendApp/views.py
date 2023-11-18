from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from BackendApp.serializers import AbonnementSerializer, CarSerializer
from BackendApp.models import Abonnement, Car

@csrf_exempt
def carApi(request, id=0):
    if request.method == 'GET' and id==0:
        cars = Car.objects.all()
        car_serializer = CarSerializer(cars, many=True)
        return JsonResponse(car_serializer.data, safe=False)
    
    elif request.method == 'GET':
        print(id)
        car = Car.objects.get(id=id)
        car_serializer = CarSerializer(car)
        return JsonResponse(car_serializer.data, safe=False)
    
    elif request.method == 'POST':
        car_data = JSONParser().parse(request)
        car_serializer = CarSerializer(data=car_data)
        if car_serializer.is_valid():
            car_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    
    elif request.method == 'PUT':
        car_data = JSONParser().parse(request)
        car = Car.objects.get(id=id)
        car_serializer = CarSerializer(car, data=car_data)
        if car_serializer.is_valid():
            car_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")
    
    elif request.method == 'DELETE':
        car = Car.objects.get(id=id)
        car.delete()
        return JsonResponse("Deleted Successfully", safe=False)

@csrf_exempt
def abonnementApi(request, id=0):
    if request.method == 'GET' and id==0:
        abonnements = Abonnement.objects.all()
        abonnement_serializer = AbonnementSerializer(abonnements, many=True)
        return JsonResponse(abonnement_serializer.data, safe=False)
    
    elif request.method == 'GET':
        print(id)
        abonnement = Abonnement.objects.get(id=id)
        abonnement_serializer = AbonnementSerializer(abonnement)
        return JsonResponse(abonnement_serializer.data, safe=False)

    elif request.method == 'POST':
        abonnement_data = JSONParser().parse(request)
        print(abonnement_data)
        abonnement_serializer = AbonnementSerializer(data=abonnement_data)
        if abonnement_serializer.is_valid():
            abonnement_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        print(abonnement_serializer.errors)
        return JsonResponse("Failed to Add", safe=False)
    
    elif request.method == 'PUT':
        abonnement_data = JSONParser().parse(request)
        abonnement = Abonnement.objects.get(id=id)
        abonnement_serializer = AbonnementSerializer(abonnement, data=abonnement_data)
        if abonnement_serializer.is_valid():
            abonnement_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")
    
    elif request.method == 'DELETE':
        abonnement = Abonnement.objects.get(id=id)
        abonnement.delete()
        return JsonResponse("Deleted Successfully", safe=False)
