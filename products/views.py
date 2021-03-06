from django.shortcuts import render, get_object_or_404
from django.http import Http404
#from django.views import Listview
from django.views.generic import ListView, DetailView

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


class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    template_name = "product/product_detail.html"

    # def get_context_data(self, *args, **kwargs):
    #     context = super(ProductListView, self).get_context_data(*args, **kwargs)
    #     return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        pk = self.kwargs.get('pk')
        return Product.objects.filter(pk=pk)


def product_detail_view(request, pk, *args, **kwargs):
    #instance = Product.objects.get(pk=pk)
    # instance = get_object_or_404(Product, pk=pk)
    instance = Product.objects.get_by_id(pk)
    print(instance)
    if instance is None:
        raise Http404("Product Does Not Exists!!")

    # qs = Product.objects.filter(id=pk)
    # if qs.exists() and qs.count() == 1:
    #     instance = qs.first()
    # else:
    #     raise Http404("Product Does Not Exists!!")
    context = {
        'object': instance
    }
    return render(request, "product/product_detail.html", context)



#Product Featured View

class ProductFeaturdListView(ListView):
    queryset = Product.objects.all().featured()
    template_name = "product/product_list.html"

    # def get_context_data(self, *args, **kwargs):
    #     context = super(ProductListView, self).get_context_data(*args, **kwargs)
    #     return context

class ProductFeaturedDetailView(DetailView):
    queryset = Product.objects.all().featured()
    template_name = "product/featured_detail.html"
    # def get_queryset(self, *args, **kwargs):
    #     request = self.request
    #     return Product.objects.featured()
    

class ProductDetailSlugView(DetailView):
    queryset = Product.objects.all()
    template_name = 'product/product_detail.html'

    def get_object(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')
        #instance = get_object_or_404(Product, slug=slug, active=True)
        try:
            instance = Product.objects.get(slug=slug, active=True)
        except Product.DoesNotExist:
            raise Http404("Not Found....")
        except Product.MultipleObjectsReturned:
            qs = Product.objects.filter(slug=slug, active=True)
            instance = qs.first()
        except:
            raise Http404("Umm ")

        return instance



    



