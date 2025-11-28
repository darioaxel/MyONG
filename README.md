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

## Vistas: Socio
* [ ] Mostrar el listado de todos los socios (sólo se muestra DNI, nombre y apellidos)
* [ ] Mostrar el detalle de un socio 

## Tareas a realizar

* [x] Actualizar el modelo de socios añadiendo tutores y roles
* [ ] Genera vistas en dos formatos: usando el modelo completo y solo con parte de él
* [ ] Configurar la aplicación para utilizar Postgres ✓
* [ ] Implementar herencia entre los tipos de socios 
* [ ] Formularios para crear un socio y validación de datos ✓
* [ ]  