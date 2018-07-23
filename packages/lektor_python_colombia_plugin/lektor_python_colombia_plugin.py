# -*- coding: utf-8 -*-
"""Custom plugin to add extra functionality to the Python Colombia site."""

# Standard library imports
from collections import OrderedDict
import os
import sys

# Local imports
from lektor.pluginsystem import Plugin
from lektor.utils import portable_popen

PY3 = sys.version_info[0] == 3


class PythonColombiaPlugin(Plugin):
    name = 'Python Colombia Custom Lektor Plugin'
    description = 'This is a custom local plugin to add extra functionality.'

    def on_after_build_all(self, *args, **kwargs):

        def run_map_generation_script():
            """Run the map generation script located at `/scripts/map.py`."""
            scripts_root = os.path.join(self.env.root_path, 'scripts')
            args = [sys.executable, os.path.join(scripts_root, 'map.py')]
            portable_popen(args, cwd=scripts_root).communicate()

        run_map_generation_script()

    def on_setup_env(self, **extra):

        def estimate_reading_time(content):
            """Estimate reading time in minutes for content."""
            words = content.split(' ')
            time = len(words)/200.0  # Avergae word reading time for adults
            return int(round(time, 0))

        self.env.jinja_env.globals.update(dir=dir)
        self.env.jinja_env.globals.update(OrderedDict=OrderedDict)
        self.env.jinja_env.globals.update(estimate_reading_time=estimate_reading_time)
