from zope import interface
from plonetheme.jquerymobile import interfaces
from plone.memoize.instance import memoize

@memoize
def getDefaultSkin(self):
    request = self.REQUEST #better way ?
    if interfaces.IThemingLayer.providedBy(request):
        return 'JQueryMobile Theme'
    return self.default_skin
