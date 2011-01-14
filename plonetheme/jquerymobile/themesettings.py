from zope import component
from zope import interface
from plone.registry.interfaces import IRegistry
from plone.app.theming.interfaces import IThemeSettings

class ThemeSettings(object):
    interface.implements(IThemeSettings)
    def __init__(self):
        self.enabled = True
        self.rules = u"python://plonetheme.jquerymobile/static/rules.xml"
        self.absolutePrefix = u""
        self.readNetwork = False
