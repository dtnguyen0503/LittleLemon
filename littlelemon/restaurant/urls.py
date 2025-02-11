from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from .views import MenuItemView, SingleMenuItemView
from rest_framework.routers import DefaultRouter

# router2 = DefaultRouter()
# router2.register(r'menu_items', MenuItemView, basename='menu-items')

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', MenuItemView.as_view(), name="menu-items"),
    path('menu/<int:pk>', SingleMenuItemView.as_view(), name='single-menu-item'),
    path('api-token-auth/', obtain_auth_token),
    #path('api/', include(router2.urls)),
]
