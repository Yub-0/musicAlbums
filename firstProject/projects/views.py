from django.http import JsonResponse, Http404
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import permissions, viewsets, status

from projects.models import Album, Track
from projects.serializers import AlbumSerializer, TrackSerializer, AlbumEditSerializer


class ListAlbumViewSet(viewsets.ViewSet):

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


class EditTrack(viewsets.ViewSet):
    def get_object(self, pk):
        try:
            return Track.objects.get(pk=pk)
        except Track.DoesNotExist:
            raise Http404

    def update(self, request, pk):
        track = self.get_object(pk)
        serializer = TrackSerializer(track, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk, format=None):
        track = self.get_object(pk)
        track.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class EditAlbum(viewsets.ViewSet):
    def get_object(self, pk):
        try:
            return Album.objects.get(pk=pk)
        except Album.DoesNotExist:
            raise Http404

    def update(self, request, pk):
        album = self.get_object(pk)
        serializer = AlbumEditSerializer(album, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk, format=None):
        album = self.get_object(pk)
        album.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
