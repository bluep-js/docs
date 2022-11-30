# Configuration file for the Sphinx documentation builder.

# -- Project information

project = '@bluepjs'
copyright = '2021-2022, Evgeny Trifonov <abrakadobr@gmail.com>'
author = 'Evgeny Trifonov'

release = '0.3'
version = '0.3.3'

# -- General configuration
import sys, os

sys.path.append(os.path.abspath('ext'))

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx_js',
    'bluep'
]

js_source_path = '../../source/vm/src'
primary_domain = 'js'

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'
