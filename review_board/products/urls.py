"""review_board URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from . import views

urlpatterns = [
    path('hello/', views.hello),
    path('', views.ProductsListView.as_view(), name='product-list'),
    path('product/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),
    path('product/add/', views.ProductCreateView.as_view(), name='product-create'),
    # path('404/', views.error_404(None, None), name='404'),
    path('product/<int:pk>/new-review/', views.ReviewCreateView.as_view(), name='new-review'),
    path('(?P<search_term>\d+)/$', views.ProductsListView.as_view(), name="searchfromurl")

]

