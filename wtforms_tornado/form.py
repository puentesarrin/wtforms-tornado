from __future__ import annotations

from collections.abc import Iterator, Mapping, Sequence
from typing import Any

from tornado import escape
from wtforms import Form as WTForm

from wtforms_tornado.i18n import TornadoTranslations


class TornadoInputWrapper(Mapping[str, Any]):
    def __init__(self, multidict: Mapping[str, Any]):
        self._wrapped = multidict

    def __iter__(self) -> Iterator[str]:
        return iter(self._wrapped)

    def __len__(self) -> int:
        return len(self._wrapped)

    def __getitem__(self, name: str) -> Any:
        return self._wrapped[name]

    def getlist(self, name: str) -> list[str]:
        try:
            values = self._wrapped[name]
        except KeyError:
            return []
        if isinstance(values, (bytes, str)) or not isinstance(values, Sequence):
            values = [values]
        return [escape.to_unicode(value) for value in values]


class Form(WTForm):
    """A WTForms form that understands Tornado arguments and locales."""

    def __init__(
        self,
        formdata: Any = None,
        obj: Any = None,
        prefix: str = '',
        locale_code: str = 'en_US',
        **kwargs: Any,
    ):
        self._locale_code = locale_code
        super().__init__(formdata=formdata, obj=obj, prefix=prefix, **kwargs)
        self._translate_labels()

    def process(
        self,
        formdata: Any = None,
        obj: Any = None,
        data: Any = None,
        extra_filters: Any = None,
        **kwargs: Any,
    ) -> None:
        if formdata is not None and not hasattr(formdata, 'getlist'):
            formdata = TornadoInputWrapper(formdata)
        super().process(formdata=formdata, obj=obj, data=data, extra_filters=extra_filters, **kwargs)
        self._translate_labels()

    def _get_translations(self) -> Any:
        return TornadoTranslations(self._locale_code)

    def _translate_labels(self) -> None:
        translations = TornadoTranslations(self._locale_code)
        for field in self:
            field.label.text = translations.gettext(field.label.text)


BaseForm = Form

__all__ = ('BaseForm', 'Form', 'TornadoInputWrapper')
