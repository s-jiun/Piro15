from django.db.models.lookups import PostgresOperatorLookup
from django.urls import path, include
from . import views

app_name = 'Posts'

urlpatterns = [
    path('', view=views.post_list, name='post_list'),
    path('create/', views.create_post, name='create_post'),
    path('like_ajax/', views.like_ajax, name='like_ajax'),
    path('add_ajax/', views.add_ajax, name='add_ajax'),
]