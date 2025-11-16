from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from .models import Place


def show_index(request):
    places = Place.objects.all().prefetch_related('imgs')
    data = {
        'type': 'FeatureCollection',
        'features': [
            {
                'type': 'Feature',
                'geometry': {
                    'type': 'Point',
                    'coordinates': [place.lng, place.lat]
                },
                'properties': {
                    'title': place.title,
                    'placeId': place.id,
                    'detailsUrl': show_place(request, place.id)
                }
            }
            for place in places
        ]
    }
    
    return render(request, 'index.html', context={'feature_collection': data})


def show_place(request, place_id):
    place_id = int(place_id)
    place = get_object_or_404(Place, pk=place_id)
    data = {
        "title": place.title,
        "imgs": [
            img.image.url
            for img in place.imgs.all()
        ],
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {
            "lng": place.lng,
            "lat": place.lat
        }
    }

    return JsonResponse(
        data,
        json_dumps_params={'ensure_ascii': False, 'indent': 4},
        content_type='application/json; charset=utf-8'
    )
