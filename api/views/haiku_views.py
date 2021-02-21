from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from django.middleware.csrf import get_token

from ..models.haiku import Haiku
from ..serializers import HaikuSerializer

class Haiku(generics.ListCreateAPIView):
    def get(self, request):
        haikus = Haiku.objects.filter(owner=request.user.id)
        data = HaikuSerializer(haikus, many=True).data
        return Response(data)
        serializer_class = HaikuSerializer

    def post(self, request):
        request.data['haiku']['owner'] = request.user.id
        print(request.data)
        haiku = HaikuSerializer(data=request.data)
        if haiku.is_valid():
            h = haiku.save()
            return Response(haiku.data, status=status.HTTP_201_CREATED)
        else:
            return Response(haiku.errors, status=status.HTTP_400_BAD_REQUEST)


class HaikuDetail(generics.RetrieveUpdateDestroyAPIView):
    def get(self, request, pk):
        haiku = get_object_or_404(Haiku, pk=pk)
        data = HaikuSerializer(haiku).data
        return Response(data)

    def delete(self, request, pk):
        haiku = get_object_or_404(Haiku, pk=pk)
        haiku.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self, request, pk):
        haiku = get_object_or_404(Haiku, pk=pk)
        data = HaikuSerializer(haiku, data=request.data['haiku'])
        if data.is_valid():
            data.save()
            return Response(data.data)
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
