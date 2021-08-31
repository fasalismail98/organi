from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('index2', views.index2, name='index2'),
    path('blog', views.blog_view, name='blog'),
    path('blog_details', views.blogdetails, name='blog-details'),
    path('checkout', views.checkout, name='checkout'),
    path('contact', views.contact, name='contact'),
    path('shop_details', views.shopdetails, name='shop-details'),
    path('shop_grid', views.shopgrid, name='shop-grid'),
    path('shoping_cart', views.shopingcart, name='shoping-cart'),
    path('signup', views.signup, name='signup'),
    path('registration', views.product_reg, name='register'),
    path('profile1',views.profile1,name='profile1'),
    path('shop',views.shop,name='shop'),
    path('productview/<int:id>',views.productview,name='productview'),
    path('cartview/<int:id>/',views.cartview,name='cartview'),
    path('cartdata/',views.cartdata,name='cartdata'),
    path('add/<int:id>/',views.add,name='add'),
    path('sub/<int:id>/',views.sub,name='sub'),
    path('cancel/<int:id>/',views.cancel,name='cancel'),
    path('order_product/',views.order_product,name='order_product'),
    path('search/',views.search,name='search'),
    path('search1/<str:data>/',views.search1,name='search1'),
]
