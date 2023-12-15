from django.urls import path,include
from Orders.views import OrderViewSet,OrderItemViewSet
from rest_framework import routers


router= routers.DefaultRouter()
router.register(r'orders',OrderItemViewSet)
#router.register(r'orderitem',OrderItemViewSet)

urlpatterns = [    
    path('',include(router.urls))     
]
