from zope import interface
from plonetheme.jquerymobile import interfaces
from plone.memoize.instance import memoize


def getDefaultSkin(self):
    request = self.REQUEST  # better way ?

    if interfaces.IThemingLayer.providedBy(request):
        return 'JQuery Mobile Theme'

    return self._old_getDefaultSkin()
