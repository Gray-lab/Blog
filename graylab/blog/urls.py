from django.urls import path

from . import views


urlpatterns = [
  path('', views.index, name='index'),
  path('entry/<str:id>', views.entry, name='entry'),
  path('entries/', views.entries, name='entries')
]