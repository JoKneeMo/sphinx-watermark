=====
Usage
=====

Configure sphinx-watermark in your ``conf.py`` file.

#. Add sphinx-watermark to the list of extensions:

   .. code-block:: bash

      extensions = ['sphinx_watermark']


#. If you are using a custom image file, specify its directory relative
   to the ``conf.py`` file. If no value is given, the path defaults to
   ``_static``.

   .. code-block:: python

      html_static_path = ['_static']


#. Enable and configure sphinx-watermark in ``conf.py``.
   You only have to include the values you want to change from default.

   Below is the bare-minimum config for an ``Internal\nDraft`` watermark:

   .. code-block:: python

      watermark = {
         'enabled': True,
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