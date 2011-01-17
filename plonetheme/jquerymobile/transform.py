#Override plone.app.theming transform component to support a specific domain
from zope import component
from zope import interface
from plone.registry.interfaces import IRegistry
from plone.app.theming import transform as base
from plone.app.theming.interfaces import IThemeSettings as baseIFace

from plonetheme.jquerymobile import interfaces


class ThemeTransform(base.ThemeTransform):
    interface.implements(base.ITransform)
    component.adapts(interface.Interface,
                     interfaces.IThemingLayer)

    def getSettings(self):
        base1 = self.request.get('BASE1')
        registry = component.getUtility(IRegistry)
        mobile = registry.forInterface(interfaces.IThemeSettings)
        if base1 != mobile.domain:
            return super(ThemeTransform, self).getSettings()
        settings = ThemeSettings()
        #hack to let cache mechanism from plone.app.theming work
        settings.__registry__ = registry.forInterface(baseIFace)
        return settings

class ThemeSettings(object):
    interface.implements(baseIFace)
    def __init__(self):
        self.enabled = True
        self.rules = u"python://plonetheme.jquerymobile/static/rules.xml"
        self.absolutePrefix = u""
        self.readNetwork = False
        #hack to let cache mechanism from plone.app.theming work
        self.__registry__ = None

