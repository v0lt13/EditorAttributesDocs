# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'EditorAttributes'
copyright = '2023, v0lt'
author = 'v0lt'

release = '1.4.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

highlight_language = "csharp"

import groundwork

html_theme = 'groundwork'

html_theme_options = {
    'collapse_navigation': False,  # Collapse navigation (False makes it tree-like)
}

epub_show_urls = 'footnote'
