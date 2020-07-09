from django.shortcuts import render
#from django.views import Listview
from django.views.generic.list import ListView

# Create your views here.
from .models import Product

class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = "product/product_list.html"

    # def get_context_data(self, *args, **kwargs):
    #     context = super(ProductListView, self).get_context_data(*args, **kwargs)
    #     return context


def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'object_list' : queryset
    }
    return render(request, "product/product_list.html", context)
