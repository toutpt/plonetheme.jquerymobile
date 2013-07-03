from zope.viewlet.interfaces import IViewletManager
from plone.app.viewletmanager.manager import OrderedViewletManager


class IHeaderLeft(IViewletManager):
    """a viewlet manager that sits on the header left"""


class IHeaderRight(IViewletManager):
    """a viewlet manager that sits on the header right"""


class IHeaderTitle(IViewletManager):
    """a viewlet manager that sits on the header center"""


class IBelowContent(IViewletManager):
    """A viewlet manager that sits at the end of the page"""


class IFooter(IViewletManager):
    """A viewlet manager that sits inside IBelowContent"""


class IPanelLeft(IViewletManager):
    """A viewlet manager that sits inside IBelowContent"""


class IPanelRight(IViewletManager):
    """A viewlet manager that sits inside IBelowContent"""


class WeightedOrderedViewletManager(OrderedViewletManager):
    """This is a new viewlet manager"""

    def sort(self, viewlets):
        """Sort the viewlets.

        ``viewlets`` is a list of tuples of the form (name, viewlet).

        This sorts the viewlets by the order looked up from the local utility
        which implements the IViewletSettingsStorage interface. The remaining
        ones are sorted just like Five does it.
        """
        results = OrderedViewletManager.sort(self, viewlets)
        def weight_cmp(x, y):
            """Compare the two objects x and y and return an integer according
            to the outcome. The return value:
            * negative if x < y,
            * zero if x == y
            * strictly positive if x > y.
            """
            xviewlet = x[1]
            yviewlet = y[1]
            xweight = getattr(xviewlet, "weight", 1000)
            yweight = getattr(yviewlet, "weight", 1000)
            if xweight < yweight:
                return -1
            elif xweight == yweight:
                return 0
            return 1

        results.sort(cmp=weight_cmp)

        return results
