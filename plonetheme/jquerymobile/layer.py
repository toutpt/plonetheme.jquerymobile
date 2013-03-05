from zope import component
from zope import interface

from plone.browserlayer import layer as base
from plone.registry.interfaces import IRegistry

from plonetheme.jquerymobile import interfaces


def mark_layer(site, event):
    base.mark_layer(site, event)
    request = event.request
    registry = component.getUtility(IRegistry)
    settings = registry.forInterface(interfaces.IThemeSettings, check=False)
    if settings and request.get('BASE1') == settings.domain:
        ifaces = [interfaces.IThemingLayer] +\
            list(interface.directlyProvidedBy(request))
        interface.directlyProvides(request, *ifaces)
