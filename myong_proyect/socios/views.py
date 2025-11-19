from django.shortcuts import render
from django.http import Http404
import json
import uuid

# Datos simulados (normalmente vendrían de la base de datos)
SOCIOS_JSON = """
[
    {
        "id": "c6f3e99b-1a20-4f6a-89a3-cc7c0a1c24f1",
        "nombre": "María",
        "apellidos": "García López",
        "fecha_nacimiento": "1990-05-12",
        "telefono": "678123456",
        "email": "maria@example.com",
        "menor_edad": false,
        "IBAN": "ES9820385778983000760236",
        "documento_identidad": "12345678A",
        "direccion": {
            "calle": "Calle Mayor",
            "numero": "10",
            "piso": "2ºB",
            "otros": "",
            "ciudad": "Valdepeñas",
            "codigo_postal": "13300",
            "provincia": "Ciudad Real",
            "pais": "España"
        }
    },
    {
        "id": "d3ad1234-9876-4567-a8b9-abcdef123456",
        "nombre": "Javier",
        "apellidos": "Martínez Ruiz",
        "fecha_nacimiento": "2005-03-02",
        "telefono": "654789321",
        "email": "javier@example.com",
        "menor_edad": true,
        "IBAN": null,
        "documento_identidad": "98765432B",
        "direccion": {
            "calle": "Avenida del Vino",
            "numero": "55",
            "piso": "",
            "otros": "Bis",
            "ciudad": "Valdepeñas",
            "codigo_postal": "13300",
            "provincia": "Ciudad Real",
            "pais": "España"
        }
    }
]
"""

# Cargar los datos JSON como lista de diccionarios
SOCIOS = json.loads(SOCIOS_JSON)


# VISTA DE LISTA DE SOCIOS
def lista_socios(request):
    return render(request, 'socio_list.html', {'socios': SOCIOS})


# VISTA DE DETALLE DE UN SOCIO
def detalle_socio(request, socio_id):
    socio = next((s for s in SOCIOS if s['id'] == str(socio_id)), None)
    if socio is None:
        raise Http404("Socio no encontrado")

    return render(request, 'socio_detail.html', {'socio': socio})
