from plone.browserlayer import layer as base
from plonetheme.jquerymobile import interfaces
from zope import component
from zope import interface
from plone.registry.interfaces import IRegistry

def mark_layer(site, event):
    base.mark_layer(site, event)
    request = event.request
    registry = component.getUtility(IRegistry)
    settings = registry.forInterface(interfaces.IThemeSettings)
    if request.get('BASE1') == settings.domain:
        ifaces = [interfaces.IThemingLayer] + list(interface.directlyProvidedBy(request))
        interface.directlyProvides(request, *ifaces)
