from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Place
from .serializers import PlaceSerializer
from rest_framework import status

@api_view(['GET'])
def get_all_places(request):
    places = Place.objects.all()
    serializer = PlaceSerializer(places, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_place(request, place_id):
    try:
        place = Place.objects.get(id=place_id)
        serializer = PlaceSerializer(place)
        return Response(serializer.data)
    except Place.DoesNotExist:
        return Response({'error': 'Place not found'}, status=404)
    
@api_view(['POST'])
def create_place(request):
    serializer = PlaceSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_Place(request, place_id):
    try:
        Place = Place.objects.get(id=place_id)
        serializer = PlaceSerializer(instance=Place, data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
        else:
             return Response(serializer.errors, status=400)
    except Place.DoesNotExist:
        return Response({'error': 'Place not found'}, status=404)

@api_view(['DELETE'])
def delete_place(request, place_id):
    try:
        place = Place.objects.get(id=place_id)
        place.delete()
        return Response({'message': 'Place deleted successfully'})
    except Place.DoesNotExist:
        return Response({'error': 'Place not found'}, status=404)
    

