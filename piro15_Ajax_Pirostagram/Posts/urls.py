from django.db.models.lookups import PostgresOperatorLookup
from django.urls import path, include
from . import views

app_name = 'Posts'

urlpatterns = [
    path('', view=views.post_list, name='post_list'),
    path('create/', views.create_post, name='create_post'),
    path('likes/', views.likes, name='likes'),
]