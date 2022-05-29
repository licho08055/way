from django.shortcuts import redirect, render,get_object_or_404

from .models import Place
from .forms import PlaceForm



def place_list(request):
    place = Place.objects.all()
    return render(request, 'places/list.html', {'place':place})


def place_detail(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    return render(request, 'places/detail.html', {'place':place})


def place_create(request):
    form = PlaceForm()
    if request.method == 'POST':
        form = PlaceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('places:place-list')
    return render(request, 'places/create.html', {'form':form}) 


def place_update(request, place_id):
    place = Place.objects.get(pk=place_id)
    form = PlaceForm(instance=place)
    if request.method == 'POST':
        form = PlaceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('places:place-list')
    return render(request, 'places/update.html', {'form':form,'place':place})


def place_delete(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    form = PlaceForm()
    if request.method == 'POST':
        form = PlaceForm(request.POST, instance=place)
    place.delete()

    return render(request, 'places/delete.html', {'place':place, 'form':form })
       