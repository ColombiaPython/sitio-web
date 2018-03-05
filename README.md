# Sitio Web de la Comunidad de Python Colombia

Este es el repositorio del sitio web de la comunidad servido por
[Github](https://colombiapython.github.io/sitio-web-desarrollo/), y
construido utilizando [lektor](https://www.getlektor.com). Se utilizó la plantilla [BINGO](http://demo.themefisher.com/themefisher/bingo/index-text.html) como base.

# Flujo de trabajo

Hay 2 ramas de git, `develop` and `production`.

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
$ pip install -U Lektor
```

### Usando conda:

```
$ conda install lektor -c conda-forge
```

## Corre el servidor local

```
$ lektor server
```

### Problemas comunes

Si en algun momento luego de instalar python3 y crear tu virtualenv. haces `lektor server` y ves este error:
```
RuntimeError: Click will abort further execution because Python 3 was configured to use ASCIas encoding for the environment.  Consult http://click.pocoo.org/python3/for mitigation steps.
```
Haz esto adentro de tu virtualenv:
```
export LC_ALL=en_us.UTF-8
export LANG=en_us.UTF-8
```
