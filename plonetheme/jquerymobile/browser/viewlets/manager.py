from zope.viewlet.interfaces import IViewletManager


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
