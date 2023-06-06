from django.urls import path
from . views import index, nuestros_servicios, quienes_somos, contactanos

urlpatterns = [
    path('', index, name='index'),
    path('nuestros_servicios/', nuestros_servicios, name='nuestros_servicios'),
    path('quienes_somos/', quienes_somos, name='quienes_somos'),
    path('contactanos/', contactanos, name='contactanos'),
]