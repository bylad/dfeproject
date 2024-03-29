"""dfesite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import debug_toolbar
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from industry import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexView.as_view(), name='index'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout', kwargs={'next_page': '/'}),
    path('industry/', include('industry.urls', namespace='industry')),
    path('price/', include('price.urls', namespace='price')),
    path('salary/', include('salary.urls', namespace='salary')),
    path('rate/', include('rate.urls', namespace='rate')),
    path('population/', include('population.urls', namespace='population')),
    path('subsidy/', include('subsidy.urls', namespace='subsidy')),
    path('docs/', include('docs.urls', namespace='docs')),
    path('__debug__/', include(debug_toolbar.urls)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
