from django.shortcuts import render, get_object_or_404
# from django.views.generic import TemplateView
from blog.models import *

# Create your views here.
# class IndexView(TemplateView):
#     template_name = 'blog/blog.html'


def posts(request, category_slug=None, subcategory_slug=None):
    category = None
    subcategory = None
    print('+++++++++++++++++++++++++++++++++++++++++++++++++++++')
    print('category_slug', category_slug)
    print('+++++++++++++++++++++++++++++++++++++++++++++++++++++')
    if category_slug:
        category = get_object_or_404(CategoryBlog, slug=category_slug)
        if subcategory_slug:
            subcategory = get_object_or_404(CategoryBlog, slug=subcategory_slug)
    seodata = BlogPage.objects.all()
    context = {'seodata': seodata,
               'category': category,
               'subcategory': subcategory}
    return render(request, 'blog/blog.html', context)
