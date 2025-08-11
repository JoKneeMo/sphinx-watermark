#!/usr/bin/env python3
# coding: utf-8
'''
A Sphinx extension that enables watermarks for HTML output.

Project Source: https://github.com/JoKneeMo/sphinx-watermark

Copyright 2024 - JoKneeMo

Licensed under GNU General Public License version 3 (GPLv3).

Commit 0762fdef2eabead5edf99e393becc2cd5a926f11 and older
are licensed under Apache License, Version 2.0 and
copyrighten 2021 by Brian Moss

Original project: https://github.com/kallimachos/sphinxmark
'''

__author__ =    'JoKneeMo <https://github.com/JoKneeMo>'
__email__ =     '421625+JoKneeMo@users.noreply.github.com'
__copyright__ = '2024 - JoKneeMo'
__license__ =   'GPLv3'
__version__ =   '2.0.0'
__keywords__ =  ['Python3', 'Sphinx', 'Extension', 'watermark']

from pathlib import Path
from shutil import copy
from string import Template
from PIL import Image, ImageDraw, ImageFont
from sphinx.application import Sphinx
from sphinx.environment import BuildEnvironment
from sphinx.util import logging
import collections

logger = logging.getLogger(__name__)

watermark_config = {
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

def generate_css(app: Sphinx, buildpath: str, imagefile: str) -> str:
    '''Create CSS file.'''
    # set default values
    repeat = 'repeat-y' if watermark_config['position']['repeat'] else 'no-repeat'
    attachment = 'fixed' if watermark_config['position']['fixed'] else 'scroll'
    position = 'center'

    if watermark_config['position']['margin'] is not None:
        css_template = Template('''${selector}.${selector_class} {
            border-${side}: 100px solid transparent;
            padding: 15px;
            -webkit-border-image: url(${image}) 20% round;
            -o-border-image: url(${image}) 20% round;
            border-image: url(${image}) 20% 100% repeat;
        }''')
    else:
        css_template = Template('''${selector}.${selector_class} {
            background-image: url("${image}") !important;
            background-repeat: ${repeat} !important;
            background-position: ${position} top !important;
            background-attachment: ${attachment} !important;
        }''')

    css = css_template.substitute(
            selector=watermark_config['selector']['type'],
            selector_class=watermark_config['selector']['class'],
            image=imagefile,
            repeat=repeat,
            attachment=attachment,
            position=position,
            side=watermark_config['position']['margin']
        )

    logger.debug(f'[watermark] Template: {css}')
    cssname = 'watermark.css'
    cssfile = Path(buildpath, cssname)

    with open(cssfile, 'w') as f:
        f.write(css)

    return cssname


def createimage(app: Sphinx, srcdir: Path, buildpath: Path) -> str:
    '''Create PNG image from string.'''
    text_content = watermark_config['text']['content']

    # draw transparent background
    width = watermark_config['text']['width']
    height = watermark_config['text']['spacing']
    img = Image.new('RGBA', (width, height), (255, 255, 255, 0))
    d = ImageDraw.Draw(img)

    # set font
    fontfile = str(Path(srcdir,'fonts', watermark_config['text']['font'] + '.ttf'))
    font = ImageFont.truetype(fontfile, watermark_config['text']['size'])

    # set x y location for text
    left, top, right, bottom = d.textbbox((-5, -20), text_content, font=font, align=watermark_config['text']['align'])
    xsize, ysize = (right - left, bottom - top)
    x = (width / 2) - (xsize / 2)
    y = (height / 2) - (ysize / 2)
    logger.debug(f'[watermark] Left: {left}, Right: {right}, Top: {top}, Bottom: {bottom}, xsize: {xsize}, ysize: {ysize}, Width: {width}, Height: {height}, x: {x}, y: {y}')

    # add text to image
    d.text((x-5, y-25), text_content, font=font, align=watermark_config['text']['align'], fill=watermark_config['text']['color'])

    # Add border around text
    padding = watermark_config['text']['border']['padding']
    border_x0 = x - padding
    border_y0 = y - padding
    border_x1 = x + xsize + padding - 5
    border_y1 = y + ysize + padding - 10
    d.rounded_rectangle([border_x0, border_y0, border_x1, border_y1], radius=watermark_config['text']['border']['radius'], fill=watermark_config['text']['border']['fill'], width=watermark_config['text']['border']['width'], outline=watermark_config['text']['border']['outline'])

    # set opacity
    img2 = img.copy()
    img2.putalpha(watermark_config['text']['opacity'])
    img.paste(img2, img)

    # rotate image
    img = img.rotate(watermark_config['text']['rotation'])

    # save image
    imagefile = f'watermark_text.png'
    imagepath = Path(buildpath, imagefile)
    img.save(imagepath, 'PNG')
    logger.debug(f"[watermark] Image saved to: {imagepath}")

    return imagefile


def get_image(app: Sphinx) -> tuple:
    '''Get image file.'''
    srcdir = Path(__file__).parent.resolve()
    confdir = str(app.confdir)

    if app.config.html_static_path:
        staticpath = app.config.html_static_path[0]
    else:
        staticpath = '_static'

    buildpath = Path(app.outdir, staticpath)

    logger.debug(f"[watermark] static path: {staticpath}")
    try:
        buildpath.mkdir()
    except OSError:
        if not buildpath.is_dir():
            raise

    if (watermark_config['image'] is not None) and (watermark_config['text']['content'] is not None):
        '''Validate selection of image or text'''
        raise TypeError('image and text.content should not *both* contain a value, remove one and try again')
    elif (watermark_config['image'] is not None) and (len(watermark_config['image']) >= 1):
        '''Copy configured image to build output'''
        imagefile = watermark_config['image']
        imagepath = Path(confdir, staticpath, imagefile)
        logger.debug(f"[watermark] Using configured image: {imagepath}")
        try:
            copy(imagepath, buildpath)
        except FileNotFoundError:
            logger.error('Unable to copy image')
            raise
    elif (watermark_config['text']['content'] is not None) and (len(watermark_config['text']['content']) >= 1):
        '''Creating an image from text content'''
        imagefile = createimage(app, srcdir, buildpath)
        logger.debug(f"[watermark] Image: {imagefile}")
    else:
        '''Final fail'''
        raise TypeError("Something went awry, it's likely that either image or text.content has a length <= 1.")

    return (buildpath, imagefile)


def generate_watermark(app: Sphinx, env: BuildEnvironment) -> None:
    '''Generate watermark'''

    if isinstance(app.config.watermark['selector'], str):
        selector_class = str(app.config.watermark['selector'])
        app.config.watermark['selector'] = {'class': selector_class}
        logger.debug(f"[watermark] Selector was a string: {app.config.watermark['selector']}")

    if isinstance(app.config.watermark['text'], str):
        text_content = str(app.config.watermark['text'])
        app.config.watermark['text'] = {'content': text_content}
        logger.debug(f"[watermark] Text was a string: {app.config.watermark['text']}")

    deep_update(watermark_config, app.config.watermark)

    logger.debug(f"[watermark] App Config: {app.config.watermark}")
    logger.debug(f"[watermark] Watermark Config: {watermark_config}")

    if watermark_config['enabled'] is True:
        logger.info('Adding watermark...', nonl=True)
        try:
            buildpath, imagefile = get_image(app)
            cssname = generate_css(app, buildpath, imagefile)
            app.add_css_file(cssname)
            logger.info(' done')
        except Exception as e:
            logger.warning(f"Failed to add watermark: {e}")
    else:
        logger.info('Not loading watermark')

    return

def deep_update(source, overrides):
    '''
    Update a nested dictionary or similar mapping.
    Modify ``source`` in place.
    '''
    for key, value in overrides.items():
        if isinstance(value, collections.abc.Mapping) and value:
            returned = deep_update(source.get(key, {}), value)
            source[key] = returned
        else:
            source[key] = overrides[key]
    return source


def setup(app: Sphinx) -> dict:
    '''Configure setup for Sphinx extension.

    :param app: Sphinx application context.
    '''
    app.add_config_value('watermark', watermark_config, 'html')
    app.connect('env-updated', generate_watermark)

    return {
        'version': __version__,
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
