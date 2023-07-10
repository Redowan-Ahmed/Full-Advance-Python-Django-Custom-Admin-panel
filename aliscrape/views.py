from django.http.response import JsonResponse
from .helpers import get_all_products_data

def get_product_data(request):
    
    get_all_products_data()
    return JsonResponse({
        'status': 200,
        'massage': 'called',
    })

""" def get_products_by_ur(request, slug):
    get_all_products_by_url_data( slug )
    return JsonResponse({
        'status': 200,
        'massage': 'called',
    }) """