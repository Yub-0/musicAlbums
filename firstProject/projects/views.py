from django.http import JsonResponse
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import permissions, viewsets

from projects.models import Album, Track
from projects.serializers import AlbumSerializer, TrackSerializer


class ListAlbumViewSet(viewsets.ViewSet):

    # queryset = Album.objects.all()
    # serializer_class = AlbumSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly,
    #                       IsOwnerOrReadOnly]
    def list(self, request):
        queryset = Album.objects.all()
        serializer = AlbumSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Album.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = AlbumSerializer(user)
        return Response(serializer.data)


# class AddAlbumViewSet(viewsets.ViewSet):
#     def create(self, request, *args, **kwargs):
#         serializer = AlbumSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save(serializer)
    # def create(self, request):
        # serializer = AlbumSerializer(data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return JsonResponse(serializer.data, status=201)
        # return JsonResponse(serializer.errors, status=400)


class TrackViewSet(viewsets.ModelViewSet):

    queryset = Track.objects.all()
    serializer_class = TrackSerializer
