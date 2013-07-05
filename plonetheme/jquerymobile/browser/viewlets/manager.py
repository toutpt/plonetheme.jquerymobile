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

try:
    from plone.app.viewletmanager.manager import WeightedOrderedViewletManager
except ImportError:
    class WeightedOrderedViewletManager(OrderedViewletManager):
        def sort(self, viewlets):
            results = super(WeightedOrderedViewletManager, self).sort(viewlets)
            def get_weight(viewlet_tuple):
                name, viewlet = viewlet_tuple
                weight = getattr(viewlet, 'weight', 0)
                try:
                    weight = int(weight)
                except ValueError:
                    weight = 0
                return weight
            results.sort(key=get_weight)
            return results
