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


.. toctree::
   :hidden:

   installation
   usage
   options
   troubleshooting
   relnotes
   source
