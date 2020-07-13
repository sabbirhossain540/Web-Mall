from django.urls import path

from .views import (
    #product_list_view, 
    ProductListView, 
    #ProductDetailView, 
    #product_detail_view,
    #ProductFeaturdListView,
    #ProductFeaturedDetailView,
    ProductDetailSlugView
)


urlpatterns = [
    path('', ProductListView.as_view()),
    path('<slug:slug>',ProductDetailSlugView.as_view())
    # path('products-fbv/', product_list_view),

    # path('products/<int:pk>', ProductDetailView.as_view()),
    # #path('products-fbv/<int:pk>', product_detail_view),

    # #Product Featured View
    # path('featured/', ProductFeaturdListView.as_view()),
    # path('featured/<int:pk>', ProductFeaturedDetailView.as_view()),

   
]
