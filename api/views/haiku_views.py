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
        return Response({ 'haikus': data })

    serializer_class = HaikuSerializer
    def post(self, request):
        request.data['haiku']['owner'] = request.user.id
        print(request.data)
        haiku = HaikuSerializer(data=request.data['haiku'])
        if haiku.is_valid():
            h = haiku.save()
            return Response(haiku.data, status=status.HTTP_201_CREATED)
        else:
            return Response(haiku.errors, status=status.HTTP_400_BAD_REQUEST)


class HaikuDetail(generics.RetrieveUpdateDestroyAPIView):
    def get(self, request, pk):
        haiku = get_object_or_404(Haiku, pk=pk)
        if not request.user.id == haiku.owner.id:
            raise PermissionDenied('Permissions Error: This is not your haiku.')
        data = HaikuSerializer(haiku).data
        return Response(data)

    def delete(self, request, pk):
        haiku = get_object_or_404(Haiku, pk=pk)
        if not request.user.id == haiku.owner.id:
            raise PermissionDenied('Permissions Error: This is not your haiku. Cannot delete')
        haiku.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk):
        haiku = get_object_or_404(Haiku, pk=pk)
        request.data['haiku']['owner'] = request.user.id
        # check that the user owns it
        if not request.user.id == haiku.owner.id:
            raise PermissionDenied('Permissions Error: This is not your haiku.')
        # print(request.data)
        h = HaikuSerializer(haiku, data=request.data['haiku'])
        if h.is_valid():
            h.save()
            return Response(h.data)
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
