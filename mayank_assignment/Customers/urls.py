from django.contrib import admin
from django.urls import path,include
from Customers.views import CustomerViewSet
from rest_framework import routers


router= routers.DefaultRouter()
router.register(r'customers',CustomerViewSet)

urlpatterns = [    
    path('',include(router.urls))
      
]
