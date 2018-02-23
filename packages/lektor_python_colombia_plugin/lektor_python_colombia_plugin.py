# -*- coding: utf-8 -*-
"""This is a custom local plugin to ad extra functionality to pybee site."""

# Standard library imports
from collections import OrderedDict
import sys

# Third party imports
from lektor.pluginsystem import Plugin


PY3 = sys.version_info[0] == 3


class PythonColombiaPlugin(Plugin):
    name = 'Python Colombia Custom Lektor Plugin'
    description = 'This is a custom local plugin to add extra functionality.'

    def on_setup_env(self, **extra):

        def estimate_reading_time(content):
            """Estimate reading time in minutes for content."""
            words = content.split(' ')
            time = len(words)/200.0  # Avergae word reading time for adults
            return round(time, 0)

        self.env.jinja_env.globals.update(dir=dir)
        self.env.jinja_env.globals.update(OrderedDict=OrderedDict)
        self.env.jinja_env.globals.update(estimate_reading_time=estimate_reading_time)
