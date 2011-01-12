from zope import interface
from zope import schema

from plone.app.theming import interfaces as base

from plonetheme.jquerymobile import i18n

class IThemingLayer(base.IThemingLayer):
    """Browser layer"""

class IThemeSettings(base.IThemeSettings):
    """Settings for jquerymobile theme"""

    domains = schema.List(
        title=i18n.label_domains,
        description=i18n.desc_domains,
        value_type=schema.TextLine(),
        required=False
        )
