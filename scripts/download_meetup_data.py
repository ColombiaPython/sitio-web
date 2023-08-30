# -*- coding: utf-8 -*-
""""""

from __future__ import unicode_literals

# Standard library imports
from datetime import datetime, timedelta
import json
import os

# Third party imports
from jinja2 import Undefined
from lektor.project import Project
import requests


HERE = os.path.abspath(os.path.dirname(__file__))
PROJECT_ROOT_PATH = os.path.dirname(HERE)


def load_api_key(name):
    """"""
    API_KEY = os.environ.get(name, None)

    if API_KEY is None:
        fpaths = [
            os.path.join(PROJECT_ROOT_PATH, name),
            os.path.join(PROJECT_ROOT_PATH, '.' + name),
            os.path.join(HERE, name),
            os.path.join(HERE, '.' + name),
        ]
        for fpath in fpaths:
            try:
                with open(fpath, 'r') as fh:
                    API_KEY = fh.read().strip()
                break
            except Exception:
                pass

    return API_KEY


def get_meetup_groups():
    """
    Loads meetup groups from the Python Colombia lektor database.

    This returns only communities that are displayed on the map.
    """
    project = Project.discover()
    env = project.make_env()
    pad = env.new_pad()
    groups = [g for g in pad.query('/usuarios/') if g['type'] == 'comunidad'
              and g['map'] and not isinstance(g['meetup_handle'], Undefined)]
    groups = {g['meetup_handle']: g['username'] for g in groups}
    return groups


class MeetupClient():
    """"""

    def __init__(self):
        """"""
        self._payload = {}

    def get_group_events(self, group_name, status='draft'):
        payload = self._payload.copy()
        payload.update({
            'status': [status],
            'page': 200,
            'group_urlname': group_name,
            #'no_earlier_than': self.date_last_month(),
            'photo-host': 'secure',
            'fields': 'featured_photo',
            'desc': 'true'
        })
        # Above is the equivalent of jQuery.extend()
        # for Python 3.5: payload = {**default_payload, **offset_payload}
        r = requests.get('https://api.meetup.com/{}/events'.format(group_name),
                         params=payload)
        if r.status_code == 200:
            json = r.json()
            events = json
        else:
            events = []
        return events

    def date_last_month(self):
        """Returns the current date minus 4 weeks in iso string format."""
        new_date = datetime.now() - timedelta(weeks=12)
        return new_date.isoformat()

    def get_events(self, group_name=None):
        """"""
        groups = [group_name] if group_name else self.GROUPS
        for group in groups:
            # draft_events = self.get_group_events(group, 'draft')
            upcoming_events = self.get_group_events(group, 'upcoming')
            # cancelled_events = self.group_events(group, 'cancelled')
            #proposed_events = self.get_group_events(group, 'proposed')
            #suggested_events = self.get_group_events(group, 'suggested')
            past_events = self.get_group_events(group, 'past')
            events = (upcoming_events + past_events)

        return events

    def save_data(self, fpath, data):
        """"""
        path = os.path.dirname(fpath)
        if not os.path.isdir(path):
            os.makedirs(path)

        with open(fpath, 'w') as fh:
            fh.write(json.dumps(data, sort_keys=True, indent=2,
                                separators=(',', ': ')))


def main():
    meetup_client = MeetupClient()
    groups = get_meetup_groups()
    print('Downloading data from Meetup API...:')
    for group in groups:
        print('\n')
        print(group)
        events = meetup_client.get_events(group)
        meetup_client.save_data(os.path.join(HERE, '.MEETUP_DATA', 'events',
                                             group + '.json'), events)


if __name__ == '__main__':
    main()
