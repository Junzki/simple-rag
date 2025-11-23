# -*- coding: utf-8 -*-
import typing as ty

import os
import pathlib
from .config import settings, SOURCE_CODE_DIR


TEMPLATE_DIRS = [
    SOURCE_CODE_DIR / "default_templates"
]
TEMPLATE_EXTENSION = ".md"


class TemplateLoader(object):

    def __init__(self, template_dirs: ty.List[pathlib.Path | str] = None,
                 template_extension: str = TEMPLATE_EXTENSION):
        self.template_dirs = TEMPLATE_DIRS
        if template_dirs:
            template_dirs.extend(template_dirs)

        self.template_extension = template_extension
        self.template_cache = dict()

    def find_template(self, template_name: str) -> pathlib.Path:
        if not template_name.endswith(self.template_extension):
            template_name += self.template_extension

        cached = self.template_cache.get(template_name)
        if cached:
            return cached

        for template_dir in self.template_dirs:
            template_path = pathlib.Path(template_dir) / template_name
            if os.path.exists(template_path):
                self.template_cache[template_name] = template_path
                return template_path

        raise FileNotFoundError(f"Template '{template_name}' not found in directories: {self.template_dirs}")

    def load_template(self, template_name: str, encoding: str = None) -> str:
        template_path = self.find_template(template_name)
        with open(template_path, 'r', encoding=encoding or 'utf-8') as f:
            template_content = f.read()

        return template_content
