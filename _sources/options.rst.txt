=======
Options
=======

:**enabled (bool)**:

   - ``True`` - enable watermarks
   - ``False`` - disable watermarks
   - Default: ``False``

   .. code-block:: python

      watermark = {
         'enabled': False
      }


:**selector (dict or string)**:

   Short form is a string, setting the class name of a div element.

   Long form is a dictionary, specifying an html element type and it's class.

   :**type (string)**:
      HTML element type to apply the watermark to.

      - Default: ``div``

   :**class (string)**:
      CSS class, applied to the type, where watermark is displayed

      - Default: ``body``
      - Examples for common themes:

        sphinx_rtd_theme -> ``'class': 'document'``

        openstackdocstheme -> ``'class': 'docs-body'``

        sphinx_book_theme -> ``'class': 'row#main-content'``

        sphinx_immaterial -> ``'class': 'md-main__inner'``

   .. code-block:: python

      watermark = {
         'selector': {
            'type': 'div',
            'class': 'body'
         }
      }

:**postion (dict)**:

   :**margin (string)**:

      - ``left`` - place watermark in the left page margin
      - ``right`` - place watermark on right page margin
      - Default: ``None``

   :**repeat (bool)**:

      - ``True`` - image repeats down the page
      - ``False`` - image appears once at top of page
      - Default: ``True``

   :**fixed (bool)**:

      - ``True`` - watermark does not scroll with content
      - ``False`` - watermark scrolls with content
      - When set to ``True``, this option centers the watermark in the viewport,
         not the element specified by ``selector``.
      - Default: ``False``

   .. code-block:: python

      watermark = {
         'position': {
            'margin': None,
            'repeat': True,
            'fixed': False
         }
      }


:**image (string)**:

   - image file name in ``html_static_path`` directory to use as watermark
   - Should not be used if text.content is set.
   - Default: ``None``

   .. code-block:: python

      watermark = {
         'image': None
      }


:**text (dict or string)**:

   Short form is a string, setting the text content and the rest default.

   Long form is a dictionary, specifying an custom options.

   :**content (string)**:
      Text to insert into the watermark.

      Use ``\n`` for multiline text.

      - Default: ``None``

   :**align** (string)**:

      - ``left`` - Left justify the text.content
      - ``right`` - Right justify the text.content
      - ``center`` - Center justify the text.content
      - Default: ``center``

   :**font (string)**:
      Which font should be used to render the text.

      - Anton
      - Gluten
      - KodeMono
      - RobotoMono
      - RubikDistressed
      - ShantellSans
      - Default: ``RubikDistressed``

   :**color (int tuple)**:
      RGB Value in as a tuple of integers

      - Default: ``(255, 0, 0)`` (Red)

   :**opacity (int)**:
      RGB Alpha, or how transparent should the watermark be

      - Default: ``40``

   :**size (int)**:
      Font size, in pixels, for the watermark text.content

      - Default: ``100``

   :**rotation (int)**:
      Degrees of rotation for the entire watermark.

      - Default: ``0``
   
   :**width (int)**:
      Width, in pixels, of transparent box containing the watermark text.content

      If a large text.size is specified, or the text.content string is long,
      you may need to set this option to a number higher than the default for
      the entire string to display.
      
      Note that the text will be cut off at the edge of the containing CSS div
      regardless of the width setting.
      
      - Default: ``816``

   :**spacing (int)**:
      Spacing, in pixels, between text watermarks when repeated, and the text line height

      - Default: ``400``

   :**border (dict)**:
      Draws a border around the watermark image.

      :**outline (int tuple)**:
         RGB Value in as a tuple of integers

         - Default: ``(255, 0, 0)`` (Red)

      :**fill (int tuple)**:
         RGB Value in as a tuple of integers to fill the watermark background.

         - Default: ``None``

      :**width (int)**:
         How wide, in pixels, the border should be.

         - Default: ``10``

      :**padding (int)**:
         How much spacing, in pixels, should be between text.content and the border.

         - Default: ``30``

      :**radius (int)**:
         How round, in pixels, the corners of the border should be.

         - Default: ``20``

   .. code-block:: python

      watermark = {
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



