from django.urls import path
from . import views

app_name = 'ideas'

urlpatterns = [
    path('', views.idea_list, name='idea_list'),
    path('ideas/<int:pk>/', views.idea_detail, name='idea_detail'),
    path('ideas/register', view=views.idea_register, name='idea_register'),
    path('ideas/<int:pk>/update/', view=views.idea_update, name='idea_update'),
    path('ideas/<int:pk>/delete/', view=views.idea_delete, name='idea_delete'),
]