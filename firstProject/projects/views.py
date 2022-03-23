from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions, viewsets

from projects.models import Album, Track
from projects.serializers import AlbumSerializer, TrackSerializer


class AlbumViewSet(viewsets.ModelViewSet):

    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly,
    #                       IsOwnerOrReadOnly]


class TrackViewSet(viewsets.ModelViewSet):

    queryset = Track.objects.all()
    serializer_class = TrackSerializer
