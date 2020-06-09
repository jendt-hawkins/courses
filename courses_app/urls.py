from django.urls import path
from . import views

urlpatterns = [
    path('', views.main),
    path('<int:id>', views.delete),
    path('no', views.no),
    path('<int:id>/yes', views.yes),
]