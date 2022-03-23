from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from projects.views import ListAlbumViewSet, TrackViewSet

album_list = ListAlbumViewSet.as_view({
    'get': 'list',
    'get': 'retrieve',
})
# album_add = AddAlbumViewSet.as_view({
#     'post': 'create'
# })
# album_detail = LAlbumViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
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
    path('albums/<int:pk>/', album_list, name='album-detail'),
    # path('addAlbums', album_add, name='album_add'),
    path('tracks/', track_list, name='track-list'),
    path('tracks/<int:pk>/', track_detail, name='track-detail')
])