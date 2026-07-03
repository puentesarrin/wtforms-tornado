from __future__ import annotations

from tornado import locale


class TornadoTranslations:
    """WTForms translations backed by Tornado locale catalogs."""

    def __init__(self, code: str):
        self.locale = locale.get(code) or locale.get('en_US')

    def gettext(self, string: str) -> str:
        return self.locale.translate(string)

    def ngettext(self, singular: str, plural: str, n: int) -> str:
        return self.locale.translate(singular, plural, n)
