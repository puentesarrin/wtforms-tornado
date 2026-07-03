===============
WTForms-Tornado
===============

WTForms extensions for Tornado.

.. image:: https://github.com/puentesarrin/wtforms-tornado/actions/workflows/ci.yml/badge.svg
   :target: https://github.com/puentesarrin/wtforms-tornado/actions/workflows/ci.yml
   :alt: CI status

.. image:: https://coveralls.io/repos/github/puentesarrin/wtforms-tornado/badge.svg?branch=master
   :target: https://coveralls.io/github/puentesarrin/wtforms-tornado?branch=master
   :alt: Coverage status

.. image:: https://img.shields.io/pypi/v/wtforms-tornado.svg
   :target: https://pypi.org/project/wtforms-tornado/
   :alt: PyPI version

WTForms-Tornado targets Python 3.11+.

Usage
=====

::

   import tornado.ioloop
   import tornado.web

   from wtforms import IntegerField
   from wtforms.validators import DataRequired
   from wtforms_tornado import Form

   class SumForm(Form):

       a = IntegerField(validators=[DataRequired()])
       b = IntegerField(validators=[DataRequired()])

   class SumHandler(tornado.web.RequestHandler):
       def get(self):
           self.write('Hello, world')

       def post(self):
           form = SumForm(self.request.arguments)
           if form.validate():
               self.write(str(form.data['a'] + form.data['b']))
           else:
               self.set_status(400)
               self.write(str(form.errors))

   application = tornado.web.Application([
       (r"/", SumHandler),
   ])

   if __name__ == "__main__":
       application.listen(8888)
       tornado.ioloop.IOLoop.current().start()

Installation
============

Install the package with pip::

   pip install wtforms-tornado

Or from a local checkout::

   pip install .

For development work, install the dev extras::

   pip install -e '.[dev]'

.. _pip: https://pip.pypa.io/
.. _PyPI: https://pypi.org/project/wtforms-tornado/
