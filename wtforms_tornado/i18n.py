# -*- coding: utf-8 -*-
from tornado import locale


class TornadoTranslations(object):
    """
    A translations object for WTForms that gets its messages from Tornado's
    locale module.
    """

    def __init__(self, code):
        self.locale = locale.get(code)

    def gettext(self, string):
        return self.locale.translate(string)

    def ngettext(self, singular, plural, n):
        return self.locale.translate(singular, plural, n)