from django.db.models.lookups import PostgresOperatorLookup
from django.urls import path, include
from . import views

app_name = 'Posts'

urlpatterns = [
    path('', view=views.post_list, name='post_list'),
]