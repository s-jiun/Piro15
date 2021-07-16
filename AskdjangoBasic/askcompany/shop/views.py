from django.shortcuts import render
from .models import Item

def item_list(request):
    qs = Item.objects.all()

    q = request.GET.get('q', '')
    if q:
        qs = qs.filter(name__icontains=q)
    return render(request, 'shop/item_list.html', {
        'item_list' : qs,
        'q' : q,
    })

# Create your views here.
