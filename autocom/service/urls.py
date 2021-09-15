from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', CategoryList.as_view(), name='category_list'),
    path('<slug:slug>/', ServiceModel.as_view(), name='service_category'),
    path('<slug:category>/<slug:slug>', ServiceModelView.as_view(), name='service_model_view'),
    path('<searchbar', views.searchbar, name='searchbar'),
]