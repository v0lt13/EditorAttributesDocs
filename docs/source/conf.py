# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'EditorAttributes'
copyright = '2025, v0lt'
author = 'v0lt'

release = '2.5.3'

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

html_theme = 'sphinx_rtd_theme'

html_theme_options = {
    'collapse_navigation': False,  # Collapse navigation (False makes it tree-like)
}

default_dark_mode = True

epub_show_urls = 'footnote'
