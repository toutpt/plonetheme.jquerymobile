from plone.app.registry.browser.controlpanel import RegistryEditForm
from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper

from plonetheme.jquerymobile.interfaces import IThemeSettings
from plone.z3cform import layout

class ThemeSettingsControlPanelForm(RegistryEditForm):
    schema = IThemeSettings

ThemeSettingsControlPanelView = layout.wrap_form(ThemeSettingsControlPanelForm,
                                                 ControlPanelFormWrapper)
