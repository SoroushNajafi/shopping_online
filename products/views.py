from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import get_object_or_404
from django.contrib import messages

from .models import Product, Comment, Category
from .forms import CommentForm


class ProductsByCategoryView(ListView):

    template_name = 'products/products_by_category.html'
    paginate_by = 3

    def get_queryset(self):
        category_id = int(self.kwargs['category_id'])
        category = get_object_or_404(Category, id=category_id)
        return category.products.all()

    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_id = int(self.kwargs['category_id'])
        category = get_object_or_404(Category, id=category_id)
        context['category'] = category
        return context


class ProductListView(ListView):
    # model = Product
    queryset = Product.objects.filter(active=True)
    template_name = 'products/product_list.html'
    context_object_name = 'products'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):

        obj = form.save(commit=False)

        obj.author = self.request.user

        product_id = int(self.kwargs['product_id'])
        product = get_object_or_404(Product, id=product_id)
        obj.product = product
        messages.success(self.request, 'comment posted')

        return super().form_valid(form)


