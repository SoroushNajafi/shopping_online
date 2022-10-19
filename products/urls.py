from django.urls import path

from .views import (ProductListView,
                    ProductDetailView,
                    CommentCreateView,
                    ProductsByCategoryView,
                    CommentDeleteView,
                    CommentUpdateView)

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('category/<int:category_id>/', ProductsByCategoryView.as_view(), name='by_category'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('comment/<int:product_id>/', CommentCreateView.as_view(), name='comment_create'),
    path('comment/delete/<int:comment_id>/', CommentDeleteView.as_view(), name='comment_delete'),
    path('comment/update/<int:comment_id>', CommentUpdateView.as_view(), name='comment_update'),
]
