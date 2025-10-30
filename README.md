# MyONG

Este proyecto va a crear una aplicación para gestionar una asociación. 
La asociación está compuesta por unos socios. 
De cada socio tendremos una serie datos personales y su dirección.

## Modelo: Socio

* [x] Identificador UUID.
* [x] DNI/NIE.
* [x] Nombre y apellidos por separado.
* [x] Fecha de nacimiento.
* [x] Teléfono

* [x] IBAN (opcional, sólo si quiere domiciliación bancaria).
* [x] Fecha de alta (auto).
* Info tutor si es menor: DNI tutor, nombre tutor, apellidos tutor y teléfono.

## Modelo: Dirección
Modificamos la primera versión para añadir un modelo con la dirección:
* Dirección con:
    * [x] calle
    * [x] número
    * [x] piso / puerta / extras (texto libre tipo "2ºB esc. izquierda")
    * [x] código postal
    * [x] ciudad (localidad)
    * [x] provincia
    * [x] país