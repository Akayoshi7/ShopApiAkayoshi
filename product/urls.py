from django.urls import path, include

from rest_framework.routers import SimpleRouter

from product import views

router = SimpleRouter()
router.register('products', views.ProductViewSet)
router.register('categories', views.CategoryViewSet)

urlpatterns = [
    path('', include(router.urls))
]