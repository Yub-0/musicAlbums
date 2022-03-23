from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from projects.views import AlbumViewSet, TrackViewSet

album_list = AlbumViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
album_detail = AlbumViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
track_list = TrackViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
track_detail = TrackViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = format_suffix_patterns([
    path('albums/', album_list, name='album-list'),
    path('albums/<int:pk>/', album_detail, name='album-detail'),
    path('tracks/', track_list, name='track-list'),
    path('tracks/<int:pk>/', track_detail, name='track-detail')
])