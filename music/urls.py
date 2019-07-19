from django.conf.urls import url
from . import views

app_name='music'

'''
urlpatterns=[
	# Default one
	url(r'^$',views.IndexView.as_view(),name='index'),
	#/register/
	url(r'^register/$',views.UserFormView.as_view(),name='register'),
	#/music/primary-key(pk)
	url(r'^(?P<pk>[0-9]+)/$',views.DetailView.as_view(),name='detail'),
	#/music/album/add/
	url(r'^album/add/$',views.AlbumCreate.as_view(),name='album-add'),
	#/music/album/2/[for editing]
	url(r'^album/(?P<pk>[0-9]+)/$',views.AlbumUpdate.as_view(),name='album-update'),
	#/music/album/2/delete/
	url(r'^album/(?P<pk>[0-9]+)/delete/$',views.AlbumDelete.as_view(),name='album-delete'),
]
'''
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<song_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),
    url(r'^songs/(?P<filter_by>[a-zA_Z]+)/$', views.songs, name='songs'),
    url(r'^create_album/$', views.create_album, name='create_album'),
    url(r'^(?P<album_id>[0-9]+)/create_song/$', views.create_song, name='create_song'),
    url(r'^(?P<album_id>[0-9]+)/delete_song/(?P<song_id>[0-9]+)/$', views.delete_song, name='delete_song'),
    url(r'^(?P<album_id>[0-9]+)/favorite_album/$', views.favorite_album, name='favorite_album'),
    url(r'^(?P<album_id>[0-9]+)/delete_album/$', views.delete_album, name='delete_album'),
]
