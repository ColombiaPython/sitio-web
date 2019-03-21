# -*- coding: utf-8 -*-
"""Custom plugin to add extra functionality to the Python Colombia site."""

# Standard library imports
from collections import OrderedDict
import os
import sys

# Third party imports
from PIL import Image as ImagePIL
from jinja2 import Undefined

# Local imports
from lektor.db import Image
from lektor.pluginsystem import Plugin
from lektor.project import Project
from lektor.reporter import reporter
from lektor.utils import portable_popen


PY3 = sys.version_info[0] == 3
PROJECT = Project.discover()
ROOT_PATH = os.path.abspath(os.path.dirname(PROJECT.project_path))
CONTENT_PATH = os.path.join(ROOT_PATH, 'content')


class PythonColombiaPlugin(Plugin):
    name = 'Python Colombia Custom Lektor Plugin'
    description = 'This is a custom local plugin to add extra functionality.'

    def on_after_build(self, builder, build_state, source, prog):
        if isinstance(source, Image) and source.parent['_model'] == 'user':
            w, h = source.width, source.height
            fpath = CONTENT_PATH + source.path
            if isinstance(w, Undefined):
                with ImagePIL.open(fpath) as img:
                    w, h = img.size

            if w != 400 and (h != 200 or h != 400):
                if fpath.endswith(source.parent['image']):
                    print('Size should be 400x400. Current size is {}x{} ({})'.format(w, h, source.path))
                elif fpath.endswith(source.parent['image_alt']):
                    print('Size should be 400x200. Current size is {}x{} ({})'.format(w, h, source.path))

            if source.parent['type'] == 'persona' and not fpath.lower().endswith(('.jpg', '.jpeg')):
                print('User images should be of type .jpg ({})'.format(source.path))

            if fpath.lower().endswith('.jpeg'):
                print('File extension should be .jpg ({})'.format(source.path))

    def on_after_build_all(self, *args, **kwargs):

        def run_map_generation_script():
            """Run the map generation script located at `/scripts/map.py`."""
            scripts_root = os.path.join(self.env.root_path, 'scripts')
            args = [sys.executable, os.path.join(scripts_root, 'map.py')]
            portable_popen(args, cwd=scripts_root).communicate()

        run_map_generation_script()
        # reporter.report_build_all_failure(10)

    def on_setup_env(self, **extra):

        def estimate_reading_time(content):
            """Estimate reading time in minutes for content."""
            words = content.split(' ')
            time = len(words)/200.0  # Average word reading speed for adults
            return int(round(time, 0))

        self.env.jinja_env.globals.update(dir=dir)
        self.env.jinja_env.globals.update(OrderedDict=OrderedDict)
        self.env.jinja_env.globals.update(estimate_reading_time=estimate_reading_time)
