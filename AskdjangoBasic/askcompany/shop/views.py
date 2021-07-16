from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound
from django.shortcuts import get_object_or_404
from shop.models import Item

# Create your views here.

def view1(request):
    try:
        item = Item.objects.get(pk=100)
    except Item.DoesNotExist:
        raise Http404

def view2(request):
    item = get_object_or_404(Item, pk=100)

def view3(request):
    try:
        item = Item.objects.get(pk=100)
    except Item.DoesNotExist:
        return HttpResponseNotFound()