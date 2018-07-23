# Sitio Web de la Comunidad de Python Colombia

[![Build Status](https://travis-ci.org/ColombiaPython/sitio-web.svg?branch=develop)](https://travis-ci.org/ColombiaPython/sitio-web)

Este es el repositorio del sitio web de la comunidad servido por
[Github](https://colombiapython.github.io/sitio-web-desarrollo/), y
construido utilizando [lektor](https://www.getlektor.com). Se utilizó la plantilla [Editorial](https://html5up.net/editorial) como base.

# Flujo de trabajo

Hay 2 ramas de git, `develop` y `production`.

## Develop

Es la rama por defecto y se despliega a través de gh-pages con Lektor a
https://colombiapython.github.io/sitio-web-desarrollo/
(en http://develop.python.org.co)

## Production

Después de que se han ejecutado las pruebas de calidad (QA), los cambios
realizados en la rama `develop` se unen con la rama `production` y son
desplegados a través de gh-pages con Lektor a 
https://colombiapython.github.io/sitio-web-produccion/
(pronto en http://www.python.org.co)

# Desarrollo local

## Instala Lektor

### Usando pip:
```
$ pip install -U Lektor unidecode
```

### Usando conda:

```
$ conda install lektor unidecode -c conda-forge
```

## Instala (reinstala) los `plugins` locales

```
$ lektor plugins reinstall
```

## Corre el servidor local

```
$ lektor server
```

## Problemas comunes

* Si en algun momento luego de instalar python3 y crear tu virtualenv. haces `lektor server` y ves este error:

```
RuntimeError: Click will abort further execution because Python 3 was configured to use ASCIas encoding for the environment.  Consult http://click.pocoo.org/python3/for mitigation steps.
```
Haz esto adentro de tu virtualenv:
```
export LC_ALL=en_us.UTF-8
export LANG=en_us.UTF-8
```

* Si ves `jinja2.exceptions.UndefinedError: 'estimate_reading_time' is undefined` significa que necesitas instalar o reinstalar los `plugins` de lektor. Puedes hacer esto ejecutando

```
$ lektor plugins reinstall
```
