from django.http import JsonResponse
from .models import Variant

def variant_list_by_make(request):
    make_id = request.GET.get("make_id")
    variants = Variant.objects.filter(make_id=make_id).values("id", "name")
    return JsonResponse(list(variants), safe=False)