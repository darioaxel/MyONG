from django.urls import path
from socios.views import detalle_socio, lista_socios, alta_socio
urlpatterns = [
    path('<uuid:socio_id>/', detalle_socio, name='detalle_socio'),
    path('', lista_socios, name='lista_socios'),
    path('alta/', alta_socio, name='alta_socio'),
]