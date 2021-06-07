from django.shortcuts import render
from rest_framework import generics
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Membership
from .serializers import MembershipSerializer
from rest_framework import status


@api_view(['GET', 'POST'])
def membership_collection(request):
    if request.method == 'GET':
        members = Membership.objects.all()
        serializer = MembershipSerializer(members, many=True)
        return Response(serializer.data)
        
    elif request.method == 'POST':
        serializer = MembershipSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def membership_element(request, pk):
    try:
        member = Membership.objects.get(pk=pk)
    except Membership.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        serializer = MembershipSerializer(member)
        return Response(serializer.data)

# def membership_registration(request):
#     if request.method == 'POST':
#         serializer = MembershipSerializer()


