# -*- coding: utf-8 -*-
"""Script to generate the content about community evnts from meetup api."""

# Standard library imports
from collections import OrderedDict
import io
import json
import os
import shutil

# Third party imports
from jinja2 import Undefined
from lektor.project import Project
from lektor.utils import slugify
from unidecode import unidecode

# Constants
HERE = os.path.abspath(os.path.dirname(__file__))
PROJECT_ROOT_PATH = os.path.dirname(HERE)
DATA_PATH = os.path.join(HERE, '.MEETUP_DATA')
MEMBERS_PATH = os.path.join(DATA_PATH, 'members')
EVENTS_PATH = os.path.join(DATA_PATH, 'events')
EVENTS_CONTENT_PATH = os.path.join(PROJECT_ROOT_PATH, 'content', 'eventos')


_ID_CACHE = {}
_SLUG_CACHE = {}

PROJECT = Project.discover()
ENV = PROJECT.make_env()
PAD = ENV.new_pad()


SLUG_WARNING_IGNORE = [
    '2018/04/pylab-ven-a-trabajar-y-compartir-tus-proyectos-de-python-en-el-vivelab',
    '2018/05/pylab-ven-a-trabajar-y-compartir-tus-proyectos-de-python-en-el-vivelab',
    '2017/07/campo-de-juego-para-emprendedores',
]


# Events that should not have been posted on meetup or events that were posted
# in more than one meetup (why??)
EVENTS_BLACKLIST = [
    'https://www.meetup.com/pythonctg/events/243208420/',
    'https://www.meetup.com/pythonbaq/events/237519744/',
    'https://www.meetup.com/Python-Cali/events/237467910/',
    'https://www.meetup.com/Python-Cali/events/237403492/',
    'https://www.meetup.com/pythonbogota/events/230113714/',
    'https://www.meetup.com/es/pythonbogota/events/257864708/'
]


def get_meetup_groups():
    """
    Loads meetup groups from the Python Colombia lektor database.

    This returns only communities that are displayed on the map.
    """
    groups = [g for g in PAD.query('/usuarios/') if g['type'] == 'comunidad'
              and g['map'] and not isinstance(g['meetup_handle'], Undefined)]
    groups = {g['meetup_handle']: g['username'] for g in groups}
    return groups


_GROUPS = get_meetup_groups()


def _meetup_address_to_lektor(event_data):
    """"""
    venue = event_data.get('venue', {})
    name = venue.get('name', '')
    address = venue.get('address_1', '')
    if name:
        name = name + '. '
    value = name + address
    return value


def _get_province(username):
    users = PAD.query('/usuarios/')
    for user in users:
        if user['username'] == username:
            province = user['province']
            break
    return province


def _meetup_date_to_date_start(event_data):
    local_date = event_data.get('local_date')
    local_time = event_data.get('local_time')
    value = local_date + ' ' + local_time + ' -0500'
    return value


def _meetup_date_to_date_end(event_data):
    return _meetup_date_to_date_start(event_data)


def _check_latlon(lat_or_lon):
    value = lat_or_lon
    if lat_or_lon and float(lat_or_lon) == 0.0:
        value = None
    return value


_LEKTOR_TO_MEETUP = OrderedDict()
_LEKTOR_TO_MEETUP['title'] = 'name'
_LEKTOR_TO_MEETUP['information'] = 'description'
_LEKTOR_TO_MEETUP['web'] = 'link'
_LEKTOR_TO_MEETUP['city'] = 'venue.city'
_LEKTOR_TO_MEETUP['country'] = 'venue.localized_country_name'
_LEKTOR_TO_MEETUP['longitude'] = 'venue.lon'
_LEKTOR_TO_MEETUP['latitude'] = 'venue.lat'
_LEKTOR_TO_MEETUP['location'] = _meetup_address_to_lektor
_LEKTOR_TO_MEETUP['date_start'] = _meetup_date_to_date_start
_LEKTOR_TO_MEETUP['date_end'] = _meetup_date_to_date_end
_LEKTOR_TO_MEETUP['__meetup_handle'] = 'group.urlname'


# _model: event-dg
# _slug: slug!!


_REPLACE = {
    ':': ' ',
    '[': ' ',
    ']': ' ',
    '.': ' ',
}


def _meetup_to_lektor_id(data):
    """"""
    local_date = data.get('local_date', '')

    name = data.get('name', '')
    _name = unidecode(name)
    for key, val in _REPLACE.items():
        _name = _name.replace(key, val)

    _name = slugify(_name)
    id_ = local_date + '-' + _name

    date_part = '/'.join(local_date.split('-')[:-1])
    slug = date_part + '/' + _name

    if id_ not in _ID_CACHE:
        _ID_CACHE[id_] = 0
        final_id = id_
    else:
        _ID_CACHE[id_] += 1
        final_id = id_ + '-' + str(_ID_CACHE[id_])

    if slug not in _SLUG_CACHE:
        _SLUG_CACHE[slug] = 0
        final_slug = slug[:]
    else:
        _SLUG_CACHE[slug] += 1

        if slug not in SLUG_WARNING_IGNORE:
            print(slug)

        final_slug = slug + '-' + str(_SLUG_CACHE[slug])

    return final_id, final_slug


def load_events():
    events = {}
    fnames = [f for f in os.listdir(EVENTS_PATH) if f != '.DS_Store']

    for fname in fnames:
        fpath = os.path.join(EVENTS_PATH, fname)

        try:
            with io.open(fpath, 'r', encoding='utf-8') as fh:
                data = fh.read()
        except Exception as e:
            print(e)
            print(fpath)

        events[fname] = json.loads(data)

    return events


def process_events_for_lektor(events):
    """"""
    events_content = OrderedDict()
    for fname, data in events.items():
        for event in reversed(events[fname]):
            if event['link'] in EVENTS_BLACKLIST:
                continue

            content = OrderedDict()
            for key, val in event.items():
                if key in ['name']:
                    id_, slug = _meetup_to_lektor_id(event)
                    content['_model'] = 'event'
                    content['_slug'] = slug

            for key, val in _LEKTOR_TO_MEETUP.items():
                if callable(val):
                    new_val = val(event)
                else:
                    new_val = event
                    parts = val.split('.')
                    for part in parts:
                        new_val = new_val.get(part, {})
                content[key] = new_val

            for key, val in content.items():
                if key in ['latitude', 'longitude']:
                    content[key] = _check_latlon(val)

            events_content[id_] = content

    return events_content


def delete_events():
    """"""
    base_path = os.path.join(PROJECT_ROOT_PATH, 'content', 'eventos')
    for path in sorted(os.listdir(base_path)):
        if (not path.endswith('contents.lr') and 'django-girls' not in path
                and '.DS_Store' not in path):
            path = os.path.join(base_path, path)
            shutil.rmtree(path)


def create_lektor_content(all_data):
    """"""
    for fname, data in all_data.items():
        meetup_handle = data.pop('__meetup_handle')
        username = _GROUPS.get(meetup_handle)
        data['province'] = _get_province(username)
        items = []
        for key, val in data.items():
            template = '{}: {}\n'
            if key in ['information']:
                val = '\n' + val

            if val:
                items.append(template.format(key, val))

        key = 'organizers'
        val = '\n\n#### organization ####\nusername: {}'.format(username)
        items.append(template.format(key, val))

        path = os.path.join(PROJECT_ROOT_PATH, 'content', 'eventos', fname)
        if not os.path.isdir(path):
            os.makedirs(path)
        fpath = os.path.join(path, 'contents.lr')

        with io.open(fpath, 'w') as fh:
            fh.write('---\n'.join(items))


def main():
    # delete_events()
    events = load_events()
    # print('\nPossible duplicates, check:')
    lektor_data = process_events_for_lektor(events)
    create_lektor_content(lektor_data)


if __name__ == '__main__':
    main()
