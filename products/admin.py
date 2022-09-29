from django.contrib import admin

from .models import Product, Comment, ProductImage, Category


class CommentsInLine(admin.TabularInline):
    model = Comment
    fields = ('author', 'body', 'stars', 'active')
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'brand', 'price', 'active')
    inlines = [CommentsInLine]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('product', 'author', 'stars', 'active')


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    fields = ('product', 'image_field',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ('category',)
