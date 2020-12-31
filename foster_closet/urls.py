"""foster_closet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.conf import settings
from django.urls import include, path, re_path   
from api import views as api_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user', api_views.UserCreateView.as_view()),
    path('api/user/<int:pk>/', api_views.UserDetailView.as_view()),
    #path('api/user/me/', api_views.current_user),
    path('api/registry/', api_views.RegistryListView.as_view()),
    path('api/registry/<int:pk>/', api_views.RegistryDetailView.as_view()),
    path('api/item/', api_views.ItemCreateView.as_view()),
    path('api/item/status/', api_views.item_list),
    path('api/item/<int:pk>/', api_views.ItemDetailView.as_view()),
    re_path(r'^auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),



]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
