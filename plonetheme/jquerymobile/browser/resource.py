from Products.Five.browser import BrowserView
from plonetheme.jquerymobile import interfaces

class IncludeCondition(BrowserView):
    """Check the include condition"""

    def __call__(self):
        return interfaces.IThemingLayer.providedBy(self.request)
