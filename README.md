<div align="center">

# Sitio Web de la Comunidad de Python Colombia

<a href="https://github.com/ColombiaPython">
  <img width="300" src="assets/static/images/about-us.jpg">
</a>

[![Build Status][build-badge]][build]
[![MIT License][license-badge]][LICENSE]
[![Python Status](https://img.shields.io/badge/Python-%3E%3D3.5-blue.svg?longCache=true&style=flat-square)](https://www.python.org/)
[![PRs Welcome][prs-badge]][prs] 
[![GitHub issues](https://img.shields.io/github/issues/ColombiaPython/sitio-web.svg?style=flat-square)](https://github.com/ColombiaPython/sitio-web/issues)
[![Twitter Jopmi](https://img.shields.io/twitter/url/http/shields.io.svg?style=social)](https://twitter.com/ColombiaPython)

Este es el repositorio del sitio web de la comunidad servido por
[Github](https://colombiapython.github.io/sitio-web-desarrollo/), y
construido utilizando [lektor](https://www.getlektor.com). Se utilizó la plantilla [Editorial](https://html5up.net/editorial) como base.

</div>

# 🔀 Flujo de trabajo

Hay 2 ramas de git, `develop` y `production`.

## ⤴️ Develop

Es la rama por defecto y se despliega a través de gh-pages con Lektor a
https://colombiapython.github.io/sitio-web-desarrollo/
(en http://develop.python.org.co)

## ⤴️ Production

Después de que se han ejecutado las pruebas de calidad (QA), los cambios
realizados en la rama `develop` se unen con la rama `production` y son
desplegados a través de gh-pages con Lektor a 
https://colombiapython.github.io/sitio-web-produccion/
(pronto en http://www.python.org.co)

# 🛠 Desarrollo local

## ✅ (Opcional) Entorno Virtual

### Instalación

Activar virtual env

* ⚠️️ Requiere previa instalación de Python ⚠️

```bash
python -m venv <nombre_entorno>
```

### Activar entorno virtual

#### Windows

```
$ <nombre_entorno>\Scripts\activate
```

#### Linux

```
$ source <nombre_entorno>/bin/activate
```

## ✅ Instala Lektor

### Usando pip:
```
$ pip install -U Lektor unidecode
```

### Usando conda:

```
$ conda install lektor unidecode -c conda-forge
```

## ✅ Instala (reinstala) los `plugins` locales

```
$ lektor plugins reinstall
```

## ✅ Corre el servidor local

```
$ lektor server
```

## ⁉️ Problemas comunes

* 🔴 Si en algun momento luego de instalar python3 y crear tu virtualenv. haces `lektor server` y ves este error:

```
RuntimeError: Click will abort further execution because Python 3 was configured to use ASCIas encoding for the environment.  Consult http://click.pocoo.org/python3/for mitigation steps.
```
Haz esto adentro de tu virtualenv:
```
export LC_ALL=en_us.UTF-8
export LANG=en_us.UTF-8
```

* 🔴 Si ves `jinja2.exceptions.UndefinedError: 'estimate_reading_time' is undefined` significa que necesitas instalar o reinstalar los `plugins` de lektor. Puedes hacer esto ejecutando

```
$ lektor plugins reinstall
```

# 🚀 Despliegue

Gracias a _Lektor Bot_ (Plugin de lektor conectado a Github), podemos desplegar nuestra web estática en diferentes repositorios (en la rama seleccionada en configuración - `gh-pages` en nuestro caso).

La configuración de dichos repositorios se encuentra en `python-colombia.lektorproject`

## ✔️ Desarrollo

```
$ lektor deploy
```

Se desplegará el contenido de la rama `develop` en `develop.python.org.co`

## ✔️✔️ Producción

```
$ lektor deploy production
```

Se desplegará el contenido de la rama `production` en `python.org.co`

# 📑 Guía de Uso

A nivel de edición contenido hay que tener en cuenta una [Guía de Uso del Sitio Web](./GUIA_DE_USO.md) ya que algunos contenidos tienen reglas especiales para poder ser agregados.

___
<div align="center">

💪 Colaboradores

|[<img src="https://avatars3.githubusercontent.com/u/3627835?s=400&v=4" width="100px;"/><br /><sub><b>Gonzalo Peña</b></sub>](https://github.com/goanpeca) | [<img src="https://avatars3.githubusercontent.com/u/14989202?s=400&v=4" width="100px;"/><br /><sub><b>Alejandro E. Rendon</b></sub>](https://github.com/arendondiosa) | [<img src="https://avatars1.githubusercontent.com/u/35072713?s=400&v=4" width="100px;"/><br /><sub><b>Nicolas Roa</b></sub>](https://github.com/nicolasroa26) |
| :---: | :---: | :---: |

</div>

[build-badge]: https://img.shields.io/travis/ColombiaPython/sitio-web.svg?style=flat-square
[build]: https://travis-ci.org/ColombiaPython/sitio-web
[license-badge]: https://img.shields.io/npm/l/all-contributors.svg?style=flat-square
[license]: https://github.com/kentcdodds/all-contributors/blob/master/LICENSE
[prs-badge]: https://img.shields.io/badge/Issues-welcome-brightgreen.svg?style=flat-square
[prs]: https://github.com/ColombiaPython/sitio-web/issues/new
[github-watch-badge]: https://img.shields.io/github/watchers/kentcdodds/all-contributors.svg?style=social
[github-watch]: https://github.com/kentcdodds/all-contributors/watchers