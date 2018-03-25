from django.urls import path

from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('company1',views.c1,name='c1'),
    path('company2',views.c2,name='c2'),
    path('company3',views.c3,name='c3'),
    path('company4',views.c4,name='c4'),
    path('company5',views.c5,name='c5'),
    path('company6',views.c6,name='c6')
]
