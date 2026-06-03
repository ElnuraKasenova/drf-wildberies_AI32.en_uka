from multiprocessing.resource_tracker import register

from django.urls import path, include
from rest_framework import routers
from .views import (UserProfileViewSet, CategoryViewSet, SubCategoryViewSet,
                    ProductListViewSet, ProductDetailViewSet, ImageProductViewSet, ReviewsViewSet,
                    CartViewSet, CartItemViewSet, FavoriteViewSet,
                    RegisterView, CustomLoginView, LogoutView)


router = routers.DefaultRouter()

router.register(r'user_profile', UserProfileViewSet, basename='user-profile')
router.register(r'category', CategoryViewSet, basename='category')
router.register(r'sub_category', SubCategoryViewSet, basename='sub_category')
router.register(r'image_product', ImageProductViewSet, basename='image-product')
router.register(r'review', ReviewsViewSet, basename='reviews')
router.register(r'cart_item', CartItemViewSet, basename='cart-item')
router.register(r'favorite', FavoriteViewSet, basename='favorite')

urlpatterns = [
    path('', include(router.urls)),

    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('product/', ProductListViewSet.as_view(), name='product-list'),
    path('product/<int:pk>/', ProductDetailViewSet.as_view(), name='product-detail'),

    path('cart/', CartViewSet.as_view(), name='cart')


]