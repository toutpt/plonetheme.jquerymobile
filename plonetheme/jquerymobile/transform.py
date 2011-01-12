from zope import component
from zope import interface
from plone.registry.interfaces import IRegistry
from plone.app.theming import transform as base

from plonetheme.jquerymobile import interfaces


class ThemeTransform(base.ThemeTransform):
    interface.implements(base.ITransform)
    component.adapts(interface.Interface,
                     interfaces.IThemingLayer)

    def getSettings(self):

        settings = super(ThemeTransform, self).getSettings()

        registry = component.getUtility(IRegistry)
        theme_settings = registry.forInterface(interfaces.IThemeSettings)
        domains = theme_settings.domains
        base1 = unicode(self.request.get('BASE1'))

        if base1 in domains:
            return theme_settings

        return settings
