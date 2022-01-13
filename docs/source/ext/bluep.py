from docutils import nodes
from docutils.parsers.rst import Directive


class BluepIDE(Directive):

  def run(self):
    paragraph_node = nodes.paragraph(text='Hello Bluep!', classes=['bluep-ide'])
    return [paragraph_node]


def setup(app):
  app.add_directive("bluepide", BluepIDE)

  return {
    'version': '0.1',
    'parallel_read_safe': True,
    'parallel_write_safe': True,
  }
