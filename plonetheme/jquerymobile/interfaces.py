from zope import interface
from zope import schema

from plone.app.theming import interfaces as base

from plonetheme.jquerymobile import i18n

class IThemingLayer(base.IThemingLayer):
    """Browser layer"""

class IThemeSettings(interface.Interface):
    """Settings for jquerymobile theme"""

    domain = schema.URI(
        title=i18n.label_domain,
        description=i18n.desc_domain,
        required=False,
        )
