from zope.viewlet.interfaces import IViewletManager


class IFooter(IViewletManager):
    """A viewlet manager that sits on the left panel"""


class IPanelLeft(IViewletManager):
    """A viewlet manager that sits on the left panel"""


class IPanelRight(IViewletManager):
    """A viewlet manager that sits on the left panel"""


class IHeaderLeft(IViewletManager):
    """a viewlet manager that sits on the header left"""


class IHeaderRight(IViewletManager):
    """a viewlet manager that sits on the header right"""
