from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Album
from .forms import AlbumForm


# Create your views here.
def index(request):
    album = Album.objects.all()
    context = {
        'album_list': album
    }

    return render(request, "index.html", context)


def details(request, alb_id):
    albde = Album.objects.get(id=alb_id)
    return render(request, "details.html", {'albde': albde})


def upload(request):
    if request.method == "POST":
        name = request.POST.get('name', )
        lyric = request.POST.get('lyric', )
        composer = request.POST.get('composer', )
        artist = request.POST.get('artist', )
        year = request.POST.get('year', )
        img = request.FILES['img']
        album = Album(name=name, lyric=lyric, composer=composer, artist=artist, year=year, img=img)
        album.save()

    return render(request, "update.html")


def edit(request, a_id):
    alb = Album.objects.get(id=a_id)
    form = AlbumForm(request.POST or None, request.FILES, instance=alb)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html', {'form': form, 'alb': alb})


def delete(request, a_id):
    if request.method == "POST":
        alb = Album.objects.get(id=a_id)
        alb.delete()
        return redirect('/')
    return render(request, 'delete.html')
