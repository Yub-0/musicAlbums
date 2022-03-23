from rest_framework import serializers

from projects.models import Album, Track


class TrackSerializer(serializers.ModelSerializer):

    class Meta:
        model = Track
        fields = ['album', 'order', 'title', 'duration']


class AlbumSerializer(serializers.ModelSerializer):
    tracks = TrackSerializer(many=True)

    class Meta:
        model = Album
        fields = ['album_name', 'artist', 'tracks']


class AlbumEditSerializer(serializers.ModelSerializer):

    class Meta:
        model = Album
        fields = ['album_name', 'artist']
