================
Sphinx Watermark
================
.. image:: https://img.shields.io/badge/License-GPL%20v3-blue.svg
   :target: https://www.gnu.org/licenses/gpl-3.0
   :alt: GPL3 License

.. image:: https://api.codeclimate.com/v1/badges/d689b89f5ae6836ad88c/maintainability
   :target: https://codeclimate.com/github/JoKneeMo/sphinx-watermark/maintainability
   :alt: Maintainability

.. image:: https://img.shields.io/pypi/status/sphinx-watermark.svg?style=flat
   :target: https://pypi.python.org/pypi/sphinx-watermark
   :alt: Project Status

.. image:: https://img.shields.io/pypi/v/sphinx-watermark.svg?style=flat
   :target: https://pypi.python.org/pypi/sphinx-watermark
   :alt: Package Version


**sphinx-watermark** is an extension for Sphinx that enables watermarks for
HTML output.

Full documentation: https://jokneemo.github.io/sphinx-watermark


***********
Why a Fork?
***********
Forked from `kallimachos/sphinxmark <https://github.com/kallimachos/sphinxmark/tree/0762fdef2eabead5edf99e393becc2cd5a926f11>`_

This fork was created primarily to remove the dependency on bottle, and to
support updates to Sphinx v7, Docutils, and Pillow.

Some themes perform differently in newer version of Docutils.
The main issues faced are html elements are changed between div, section,
article, etc.

Sphinxmark only supported div elements and the configuration changes I made to
support it were too expansive for a simple pull request. See below for all of
the enhancements added.


What's Different?
~~~~~~~~~~~~~~~~~
- Removed bottle dependency
- HTML element selection
- Static png name to support spaces in text
- Collection of fonts

  - See the `fonts directory <https://github.com/JoKneeMo/sphinx-watermark/tree/main/sphinx_watermark/fonts>`_.

- Customizable border


************
Installation
************

Install sphinx-watermark using pip:

.. code-block:: bash

   $ pip3 install sphinx-watermark


Usage
~~~~~

#. Add sphinx-watermark to the list of extensions in ``conf.py``:

   .. code-block:: python

      extensions = ['sphinx_watermark']

#. Enable and configure sphinx-watermark in ``conf.py``.
   You only have to include the values you want to change from default.

   Below is the bare-minimum config for an ``Internal Draft`` watermark:

   .. code-block:: python

      watermark = {
         'enabled': False,
         'text': 'Internal\nDraft'
      }


   Below are the defaults for all options:
   (Notice that watermarks are disabled by default.)

   .. code-block:: python
      :emphasize-lines: 2,14

      watermark = {
         'enabled': False,
         'selector': {
            'type': 'div',
            'class': 'body'
         },
         'position': {
            'margin': None,
            'repeat': True,
            'fixed': False
         },
         'image': None,
         'text': {
            'content': None,
            'align': 'center',
            'font': 'RubikDistressed',
            'color': (255, 0, 0),
            'opacity': 40,
            'size': 100,
            'rotation': 0,
            'width': 816,
            'spacing': 400,
            'border': {
                  'outline': (255, 0, 0),
                  'fill': None,
                  'width': 10,
                  'padding': 30,
                  'radius': 20,
            }
         }
      }

#. Build your docs as normal. The defined watermark should appear behind the text.

   .. note::

      Some Sphinx themes place body content in different CSS divs.
      See the `sphinx-watermark documentation <https://jokneemo.github.io/sphinx-watermark/>`_
      for full configuration details.
