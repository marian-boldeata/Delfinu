from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="index"),
    path("products/", views.products_list, name="products"),
    path("products/<int:product_id>", views.single_product, name="one_product"),
    path("about/", views.about, name= "about")

]

