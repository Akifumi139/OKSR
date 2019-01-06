from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('See/', views.See, name='See'),
    path('Write/', views.Write, name='Write'),
    path('Write/camera/', views.take_img, name='take_img'),
]
