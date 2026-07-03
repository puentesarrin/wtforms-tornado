"""WTForms extensions for Tornado."""

from __future__ import annotations

from wtforms_tornado.form import BaseForm, Form, TornadoInputWrapper
from wtforms_tornado.i18n import TornadoTranslations

__author__ = 'Jorge Puente Sarrín <puentesarrin@gmail.com>'
__since__ = '2013-09-25'
__version__ = '0.0.3.dev0'
version = __version__

__all__ = ('BaseForm', 'Form', 'TornadoInputWrapper', 'TornadoTranslations', 'version', '__version__')
