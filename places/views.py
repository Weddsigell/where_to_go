from django.shortcuts import render
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
                    'detailsUrl': ''
                }
            }
            for place in places
        ]
    }
    return render(request, 'index.html', context={'feature_collection': data})

                    # 'detailsUrl': {
                    #     'imgs': [f'{img.image.url}' for img in place.imgs.all()],
                    #     'description_short': place.description_short,
                    #     'description_long': place.description_long,
                    # }