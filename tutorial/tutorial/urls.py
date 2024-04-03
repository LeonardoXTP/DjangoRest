from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from quickstart import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# Cablear nuestra API utilizando el enrutamiento automático de URL.
#Además, incluimos URL de inicio de sesión para la API navegable.

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]