from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from projects.views import ListAlbumViewSet, ListSpecificAlbum, AddAlbumViewSet, ListTrackViewSet, ListSpecificTrack, AddTrackViewSet, EditTrack, EditAlbum

album_list = ListAlbumViewSet.as_view({
    'get': 'list',
})
album_list_specific = ListSpecificAlbum.as_view({
    'get': 'retrieve'
})
album_add = AddAlbumViewSet.as_view({
    'post': 'create'
})

track_list = ListTrackViewSet.as_view({
    'get': 'list',
})
track_list_specific = ListSpecificTrack.as_view({
    'get': 'retrieve',
})
track_add = AddTrackViewSet.as_view({
    'post': 'create'
})
# album_detail = LAlbumViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })

track_edit = EditTrack.as_view({
    'put': 'update',
    # 'put': 'partial_update'
    'delete': 'destroy'
})
album_edit = EditAlbum.as_view({
    'put': 'update',
    'delete': 'destroy'
})

urlpatterns = format_suffix_patterns([
    path('albums/', album_list, name='album-list'),
    path('albums/<int:pk>/', album_list_specific, name='album-detail'),
    path('addAlbums', album_add, name='album_add'),
    path('tracks/', track_list, name='track-list'),
    path('tracks/<int:pk>/', track_list_specific, name='track-detail'),
    path('addTracks', track_add, name='track_add'),
    path('editTracks/<int:pk>/', track_edit, name='track_edit'),
    path('editAlbums/<int:pk>', album_edit, name='album_edit')

])