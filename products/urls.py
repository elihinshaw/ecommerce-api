from django.urls import path
from .views import ProductsView


urlpatterns = [
    path("products-view/", ProductsView.as_view(), name="products-view"),
]
