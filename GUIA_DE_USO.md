<div align="center">

# Guía de Uso - Sitio Web de la Comunidad de Python Colombia

<a href="https://github.com/ColombiaPython">
  <img width="300" src="assets/static/images/about-us.jpg">
</a>
</div>

___

## Django Girls Colombia `/django-girls-colombia`

### Agregar Miembros

A petición del _Equipo Django Girls Colombia_, se modifica la vista para que la sección de `Equipo` se divida en dos apartados: `Core Team` y `Colaboradores`.

Al entrar a la vista `/admin` que proporciona _Lektor_, se observa en la sección de `Miembros`:

![Admin Miembros](assets/static/images/documentation/dg_add_member.png)

El valor agregado en el campo `Cargo`, define el apartado del Equipo en donde aparecerá el miembro:

* `core`: Core team
* `equipo`: colaboradores

## Eventos `/eventos`

### Eventos en `meetup.com`

Los scripts que se encargan de traer la información de los eventos de las comunidades locales:

* `/scripts/create_events.py`
* `/scripts/download_meetup_data.py`

Es necesario crear un archivo `MEETUP_API_KEY` para obtener la información.

> Pronto más información