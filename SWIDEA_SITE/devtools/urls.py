from django.urls import path
from . import views

app_name = 'devtools'

urlpatterns = [
    path('devtools/', views.devtool_list, name='devtool_list'),
    path('devtools/<int:pk>/', views.devtool_detail, name='devtool_detail'),
    path('devtools/register', view=views.devtool_register, name='devtool_register'),
    path('devtools/<int:pk>/update/', view=views.devtool_update, name='devtool_update'),
    path('devtools/<int:pk>/delete/', view=views.devtool_delete, name='devtool_delete'),
]