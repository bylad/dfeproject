from django.contrib import admin
from blog.models import BlogPage, CategoryBlog


class BlogPageAdmin(admin.ModelAdmin):
    list_display = ('h1',)


class CategoryBlogAdmin(admin.ModelAdmin):
    list_display = ('title',)


# Register your models here.
admin.site.register(BlogPage, BlogPageAdmin)
admin.site.register(CategoryBlog, CategoryBlogAdmin)
