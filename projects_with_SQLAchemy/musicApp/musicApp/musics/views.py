from django.http import HttpResponse
from django.shortcuts import render, redirect

from musicApp.common.session_decorator import session_decorator
from musicApp.musics.forms import AlbumCreateForm, SongCreateForm, AlbumEditForm, AlbumDeleteForm
from musicApp.musics.models import Album, Song
from musicApp.settings import session


@session_decorator(session)
def index(request):
    albums = session.query(Album).all()

    context = {
        "albums": albums
    }
    return render(request, "common/index.html", context)


def create_album(request):
    if request.method == "POST":
        form = AlbumCreateForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = AlbumCreateForm()

    context = {
        "form": form
    }
    return render(request, "albums/create-album.html", context)


@session_decorator(session)
def details_album(request, pk: int):
    album = (session
             .query(Album)
             .filter(Album.id == pk)
             .first()
             )

    context = {
        "album": album
    }

    return render(request, "albums/album-details.html", context)


@session_decorator(session)
def edit_album(request, pk: int):
    album = (session
             .query(Album)
             .filter(Album.id == pk)
             .first()
             )

    if request.method == "POST":
        form = AlbumEditForm(request.POST)

        if form.is_valid():
            form.save(album)
            return redirect("index")
    else:
        initial_data = {
            "album_name": album.album_name,
            "image_url": album.image_url,
            "price": album.price
        }

        form = AlbumEditForm(initial=initial_data)

    context ={
        "form": form,
        "album": album,
    }

    return render(request, "albums/edit-album.html", context)


@session_decorator(session)
def delete_album(request, pk: int):
    album = (session
             .query(Album)
             .filter(Album.id == pk)
             .first()
             )

    if request.method == "POST":
        session.delete(album)
        return redirect("index")
    else:
        initial_data = {
            "album_name": album.album_name,
            "image_url": album.image_url,
            "price": album.price
        }

        form = AlbumDeleteForm(initial=initial_data)

    context = {
        "form": form,
        "album": album,
    }

    return render(request, "albums/delete-album.html", context)


@session_decorator(session)
def create_song(request):
    if request.method == "POST":
        form = SongCreateForm(request.POST, request.FILES)

        if form.is_valid():
            form.save(request)
            return redirect("index")
    else:
        form = SongCreateForm()

    context = {
        "form": form
    }

    return render(request, "songs/create-song.html", context)


@session_decorator(session)
def serve_song(request, pk):
    song = (session
            .query(Song)
            .filter(Song.id == pk)
            .first()
            )

    if song:
        response = HttpResponse(song.music_file_data, content_type="audio/mpeg")
        response["Content-Disposition"] = f'inline; filename="{song.song_name}"'
        return response
    else:
        return HttpResponse("Song not found", status=404)


@session_decorator(session)
def play_song(request, pk):
    song = (session
            .query(Song)
            .filter(Song.id == pk)
            .first()
            )

    context = {
        "song": song
    }

    return render(request, 'songs/music-player.html', context)

