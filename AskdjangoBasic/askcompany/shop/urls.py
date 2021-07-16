from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('1/', view=views.view1, name='view1'),
    path('2/', view=views.view2, name='view2'),
    path('3/', view=views.view3, name='view3'),
]