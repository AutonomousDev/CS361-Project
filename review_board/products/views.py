from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.shortcuts import get_object_or_404
from .models import Product, Review
from django.db.models import Q
from .bw_helper import black_white
from django.core.files import File
from django.conf import settings

def hello(request):
    text = """<h1>welcome to my app !</h1>"""
    return render(request, "products/hello.html", {})


class ProductsListView(ListView):
    context_object_name = "products"
    template_name = "products/products.html"

    def get_queryset(self, *args, **kwargs):
        query = self.request.GET.get("q")
        object_list = None
        if query is None:
            object_list=Product.objects.all()
        else:
            object_list = Product.objects.filter(
                Q(name__icontains=query) | Q(brand__icontains=query)
            )
        return object_list


class ProductDetailView(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Reviews'] = Review.objects.filter(product=self.get_object())
        return context


class ProductCreateView(CreateView):
    model = Product
    fields = ['name', 'brand', 'description', 'product_image']

    def form_valid(self, form):
        obj = form.save(commit=False)
        image = obj.product_image
        black_white(image)
        bw_image = open(settings.MEDIA_ROOT + "/resized.jpeg", "rb")
        image.save("image.jpg", File(bw_image), save=True)
        obj.save()
        return super().form_valid(form)


class ReviewCreateView(CreateView):
    model = Review
    fields = ['title', 'comments']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Product'] = Product.objects.get(id=self.kwargs.get('pk'))
        return context

    def form_valid(self, form):
        form.instance.product = get_object_or_404(Product, id=self.kwargs.get('pk'))  # new line
        return super().form_valid(form)


def error_404(request, exception):
    return render(request, '404.html', status=404)



