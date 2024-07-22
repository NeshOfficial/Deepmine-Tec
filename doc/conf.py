# Copyright 2024 Your Organization
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Configuration file for the Sphinx documentation builder."""

import os
import sys

# -- Path setup --------------------------------------------------------------
sys.path.insert(0, os.path.abspath('../src'))
sys.path.append(os.path.abspath('extensions'))

from sphinxcontrib import katex
from sphinxcontrib import youtube

# -- Project information -----------------------------------------------------
project = 'MuJoCo'
copyright = '2024 Your Organization'  # Updated copyright year
author = 'Your Organization'  # Updated author

# -- General configuration ---------------------------------------------------
master_doc = 'index'

extensions = [
    'sphinxcontrib.bibtex',
    'sphinxcontrib.katex',
    'sphinxcontrib.youtube',
    'sphinx_copybutton',
    'sphinx_favicon',
    'sphinx_reredirects',
    'sphinx_toolbox.collapse',
    'sphinx_toolbox.github',
    'sphinx_toolbox.sidebar_links',
    'mujoco_include',
]

github_username = 'your-organization'
github_repository = 'mujoco'

bibtex_bibfiles = ['references.bib']

templates_path = ['templates']

exclude_patterns = [
    '_build',
    'Thumbs.db',
    '.DS_Store',
    'includes/*',
    'APIreference/functions.rst',
    'APIreference/functions_override.rst',
    'XMLschema.rst',
]

redirects = {
    'index': 'overview.html',
    'computation': 'computation/index.html',
    'programming': 'programming/index.html',
    'APIreference': 'APIreference/index.html',
}

rst_prolog = """
.. include:: /includes/macros.rst
.. include:: /includes/roles.rst
"""

# -- Options for autodoc -----------------------------------------------------
autodoc_default_options = {
    'member-order': 'bysource',
    'special-members': True,
    'exclude-members': '__repr__, __str__, __weakref__',
}

# -- Options for HTML output -------------------------------------------------
html_theme = 'furo'
html_title = 'MuJoCo Documentation'
html_logo = 'images/new_logo.svg'  # Updated logo file

SHARED_CSS_VARIABLES = {
    'admonition-font-size': '1rem',
    'admonition-title-font-size': '1rem',
    'sidebar-item-font-size': '130%',
}

html_theme_options = {
    'light_css_variables': {
        'font-stack--monospace': 'Inconsolata,Consolas,ui-monospace,monospace',
        'at-color': '#830b2b',
        'at-val-color': '#bc103e',
        'body-color': '#14234b',
        'color-highlight-on-target': '#e5e8ed',
        'primary-header-color': '#0053d6',
        'row-odd-background-color': '#f0f3f7',
        'rst-content-a-color': '#2980b9',
        'secondary-header-color': '#123693',
        'wy-menu-vertical-background-color': '#0053d6',
        'wy-menu-vertical-color': 'white',
        'wy-nav-side-background-color': '#0053d6',
    },
    'dark_css_variables': {
        'at-color': '#ffaab7',
        'at-val-color': '#ff95a6',
        'body-color': '#14234b',
        'color-admonition-background': '#1e1e21',
        'color-highlight-on-target': '#3d4045',
        'primary-header-color': '#a8caff',
        'row-odd-background-color': '#222326',
        'rst-content-a-color': '#2980b9',
        'secondary-header-color': '#458dff',
        'wy-menu-vertical-background-color': '#0053d6',
        'wy-menu-vertical-color': 'white',
        'wy-nav-side-background-color': '#0053d6',
    },
}

for v in html_theme_options.values():
    if isinstance(v, dict):
        v.update(SHARED_CSS_VARIABLES)

pygments_style = 'sphinx'
pygments_dark_style = 'monokai'

html_static_path = [
    '_static',
    'css',
]
html_css_files = [
    'theme_overrides.css',
]

favicons = [
    {
        'sizes': '16x16',
        'href': 'favicons/favicon-16x16.png',
    },
    {
        'sizes': '32x32',
        'href': 'favicons/favicon-32x32.png',
    },
    {
        'rel': 'apple-touch-icon',
        'sizes': '180x180',
        'href': 'favicons/favicon-180x180.png',
    },
]

# -- Options for katex ------------------------------------------------------
latex_macros = r"""
    \def \d              #1{\operatorname{#1}}
    \def \ar             {a_{\rm ref}}
    \def \au             {a_0}
    \def \ac             {a_1}
    \def \ari            {a_{{\rm ref},i}}
    \def \aui            {a_{0,i}}
    \def \aci            {a_{1,i}}
"""

katex_macros = katex.latex_defs_to_katex_macros(latex_macros)
katex_options = 'macros: {' + katex_macros + '}'

latex_elements = {'preamble': latex_macros}
