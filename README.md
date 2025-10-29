# MyONG

Este proyecto va a crear una aplicación para gestionar una asociación. 
La asociación está compuesta por unos socios. 
De cada socio tendremos una serie datos personales y su dirección.

## Modelo: Socio

* Identificador UUID.
* DNI/NIE.
* [ x ] Nombre y apellidos por separado.
* [ x ] Fecha de nacimiento.
* [ x ] Teléfono
* Dirección con:
    * calle
    * número
    * piso / puerta / extras (texto libre tipo "2ºB esc. izquierda")
    * código postal
    * ciudad (localidad)
    * provincia
    * país

* [ x ] IBAN (opcional, sólo si quiere domiciliación bancaria).
* [ x ] Fecha de alta (auto).
* Info tutor si es menor: DNI tutor, nombre tutor, apellidos tutor y teléfono.