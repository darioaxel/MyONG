from django.urls import path
from socios.views import detalle_socio
urlpatterns = [
    path('<uuid:socio_id>/', detalle_socio, name='detalle_socio')
]