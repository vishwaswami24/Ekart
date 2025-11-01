from django.urls import path
from vapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('products',views.products),
    path('about',views.about),
    path('contact',views.contact),
    path('login',views.user_login),
    path('register',views.register),
    path('logout',views.user_logout),
    path('catfilter/<cv>',views.catfilter),
    path('sort/<sv>',views.sortprice),
    path('pricefilter',views.pricefilter),
    path('product_details/<pid>',views.product_details),
    path('placeorder',views.placeorder),
    path('addcart/<pid>',views.cart),
    path('viewcart',views.viewcart), 
    path('updateqty/<x>/<cid>',views.updateqty),
    path('removecart/<cid>',views.removecart),
    path('fetchorder',views.fetchorderdetails),
    path('makepayment',views.makepayment),
    path('paymentsuccess',views.paymentsuccess),
    path('removeord/<oid>',views.removeord),
    path('profile',views.profile),
    path('api/cart-count/', views.cart_count, name='cart_count'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
