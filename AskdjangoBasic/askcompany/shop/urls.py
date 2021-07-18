from django.urls import path, re_path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.item_list),
    path('<int:pk>/', views.item_detail),
    # re_path(r'^(?P<pk>\d+)/$', views.item_detail),
]