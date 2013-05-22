from plone.app.layout.viewlets.common import (
    ViewletBase,
    GlobalSectionsViewlet,
)
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plonetheme.jquerymobile import i18n
_ = i18n._


class BaseHeaderAction(ViewletBase):
    """This is the base header action class
    it generate all nice jquerymobile options you want

    <a href="#panel-left"
       data-role="button"
       data-icon="bars" data-iconpos="notext"></a>
    """
    index = ViewPageTemplateFile("templates/base_header_action.pt")
    href = ""
    icon = ""
    iconpos = "notext"
    label = ""

    def render(self):
        if self.is_available():
            return self.index()
        return ""

    def is_available(self):
        return True


class PanelLeftAction(BaseHeaderAction):
    href = "string:#panel-left"
    icon = "bars"
    iconpos = "notext"
    label = _(u"Open left panel")


class PanelRightAction(BaseHeaderAction):
    href = "string:#panel-right"
    icon = "grid"
    iconpos = "notext"
    label = _(u"Open right panel")

    def is_available(self):
        plone_view = self.context.restrictedTraverse('@@plone')
        return plone_view.have_portlets('plone.rightcolumn', self.context)


class GlobalSections(GlobalSectionsViewlet):
    index = ViewPageTemplateFile("templates/sections.pt")
