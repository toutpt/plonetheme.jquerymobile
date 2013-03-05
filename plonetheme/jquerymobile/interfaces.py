from zope import interface

from plone.app.theming import interfaces as base


class IThemingLayer(base.IThemingLayer):
    """Browser layer"""


class IJqueryMobileView(interface.Interface):
    """The view for mobile site"""

    def apply_to_context():
        """Return true if you are suppose to apply this view on the context

        This is the entry point for integrator wants to support other add-ons"""

