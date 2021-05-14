from django.urls import path
from blog.views import *

app_name = 'blog'

urlpatterns = [
    path('<slug:category_slug>/<slug:subcategory_slug>/', posts, name='subcategory_posts'),
    path('<slug:category_slug>/', posts, name='category_posts'),
    path('', posts, name='posts'),
    # path('', views.IndexView.as_view(), name='blog'),
    # path('<int:pk>/', views.IndustryNewsDetailView.as_view(), name='blog_detail'),
]