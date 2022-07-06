from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic import DetailView
from django.views import View

from django.views.generic.edit import CreateView, DeleteView, UpdateView


from django.http import HttpResponse
from .models import Product


def hello(request):
    text = """<h1>welcome to my app !</h1>"""
    return render(request, "products/hello.html", {})
# Create your views here.


class ProductsListView(ListView):
    queryset = Product.objects.all()
    context_object_name = "products"
    template_name = "products/products.html"


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    fields = ['name', 'brand', 'description']

    def form_valid(self, form):
        return super().form_valid(form)


def error_404(request, exception):
    return render(request, '404.html', status=404)
