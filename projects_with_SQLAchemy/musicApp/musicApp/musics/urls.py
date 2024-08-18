from django.urls import path, include

from musicApp.musics import views

urlpatterns = [
    path("", views.index, name="index"),
    path("album/", include([
        path("create-album", views.create_album, name="create album"),
        path("details/<int:pk>", views.details_album, name="details album"),
        path("edit/<int:pk>", views.edit_album, name="edit album"),
        path("delete/<int:pk>", views.delete_album, name="delete album")
    ])),
    path("song/", include([
        path("create/", views.create_song, name="create song"),
        path("serve-song/<int:pk>", views.serve_song, name="serve song"),
        path("play-song/<int:pk>", views.play_song, name="play song")
    ])),
]
