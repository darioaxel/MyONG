from django.urls import path
from socios.views import detalle_socio, lista_socios, alta_socio, pagos_socio_ano
urlpatterns = [
    path('<uuid:socio_id>/', detalle_socio, name='detalle_socio'),
    path('', lista_socios, name='lista_socios'),
    path('alta/', alta_socio, name='alta_socio'),
    path('<uuid:socio_id>/pagos/', pagos_socio_ano, name='pagos_socio_ano'),
]