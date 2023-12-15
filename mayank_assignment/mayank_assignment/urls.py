from django.contrib import admin
from django.urls import path,include
from Customers.views import *
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include('Customers.urls')),
    path("api/",include('Customers.urls')),
    path("api/",include('Products.urls')),
    path("api/",include('Orders.urls')),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/docs/', SpectacularSwaggerView.as_view(url_name='schema')),
]


