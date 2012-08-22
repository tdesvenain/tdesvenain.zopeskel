import copy
import os

from zopeskel.base import get_var
from zopeskel.plone import Plone

class EDM(Plone):
    """Addon for Plone"""
    _template_dir = "templates/tdesvenain_edm"
    summary= u"A plone policy package for an edm project"

    use_local_commands = False #or setup.cfg will be re created

    vars = copy.deepcopy(Plone.vars)
    get_var(vars, 'description').default = 'Addon for Plone'
    get_var(vars, 'url').default =  'https://github.com/tdesvenain/'
