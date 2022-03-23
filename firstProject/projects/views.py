from django.http import JsonResponse
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import permissions, viewsets, status

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


class ListSpecificAlbum(viewsets.ViewSet):
    def retrieve(self, request, pk=None):
        queryset = Album.objects.all()
        album = get_object_or_404(queryset, pk=pk)
        serializer = AlbumSerializer(album)
        return Response(serializer.data)


class AddAlbumViewSet(viewsets.ViewSet):
    def create(self, request, *args, **kwargs):
        serializer = AlbumSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    # def create(self, request, *args, **kwargs):
    #
    #     serializer = AlbumSerializer(data=request.data)
    #     print("here hello")
    #     if serializer.is_valid(raise_exception=True):
    #         serializer.save(serializer)
    #         return JsonResponse(serializer.data, status=201)
    #     return JsonResponse(serializer.errors, status=400)


class AddTrackViewSet(viewsets.ViewSet):
    def create(self, request, *args, **kwargs):
        serializer = TrackSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ListTrackViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Track.objects.all()
        serializer = TrackSerializer(queryset, many=True)
        return Response(serializer.data)


class ListSpecificTrack(viewsets.ViewSet):
    def retrieve(self, request, pk=None):
        queryset = Track.objects.all()
        track = get_object_or_404(queryset, pk=pk)
        serializer = TrackSerializer(track)
        return Response(serializer.data)

