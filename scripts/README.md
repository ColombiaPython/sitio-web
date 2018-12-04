# Actualización de los eventos de la comunidad en Python Colombia

En esta carpeta se encuentran los *scripts* necesarios para descargar la
información de las diferentes comunidades y grupos de Meetups y crear los
eventos usando el API de Meetup https://www.meetup.com/es/meetup_api/

* `map.py`: Este archivo se utiliza a manera de plugin dentro de Lektor.
No es necesario ejecutarlo manualmente
* `download_meetup_data.py`: Este archivo se utiliza para descargar la
información de eventos usando el API de Meetup. Requiere un API Key.
* `create_events.py`: Este archivo crea nuevo contenido de eventos en Lektor
basado en la información descargada por `download_meetup_data.py`

## Dependencias

Para poder ejecutar estos scripts, es necesario tener instalado los siguientes
paquetes

```
Lektor
meetup-api
```

### Usando pip

Utilizando `pip` las dependencias se pueden instalar ejecutando

```
$ pip install lektor meetup-api
```

## Meetup API Key

Para poder ejecutar el archivo `download_meetup_data.py` es necesario crear un
archivo `/scripts/.MEETUP_API_KEY` que contenga la llave del API, la cual está
utilizando la cuenta del bot de python colombia en meetup.

Preguntar a [@goanpeca](https://github.com/goanpeca) y
[@arendondiosa](https://github.com/arendondiosa) por más información

## Meetup Data

Al ejecutar `download_meetup_data.py`, la información se descarga en la carpeta
`/scripts/.MEETUP_DATA`, la cual no está lleva en control de versión.

## Actualización eventos

El proceso completo de actualización de eventos requiere ejecutar los
siguientes comandos en la terminal:

```
$ python scripts/download_meetup_data.py
$ python scripts/create_events.py
```
