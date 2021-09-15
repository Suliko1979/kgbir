from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DetailView

class CategoryList(ListView):
    model = Category
    queryset = Category.objects.all()
    context_object_name = 'categories'
    template_name='service/index.html'

class ServiceModel(ListView):
    """Список товаров по категориям"""
    model = Model
    context_object_name = 'service_category'
    template_name = 'service/service_category.html'

    def get_queryset(self):
        return Model.objects.filter(category__slug=self.kwargs.get('slug'))

class ServiceModelView(DetailView):
    """Отображение отдельного товара из категории"""
    model = Model
    context_object_name = 'service_model_view'
    template_name = 'service/service_model.html'

    def get_queryset(self):
        return Model.objects.filter(category__slug=self.kwargs.get('category'), slug=self.kwargs.get('slug'))


def searchbar(request):
    if request.method =='GET':
        search = request.GET.get('search')
        model = Model.objects.all().filter(title=search)
        return render(request, 'searchbar.html', {'model': model})

# https://www.youtube.com/watch?v=3ZrH6CHIS90











