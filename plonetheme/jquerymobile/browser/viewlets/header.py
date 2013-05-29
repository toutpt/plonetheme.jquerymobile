from zope import component
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


class SearchRightAction(BaseHeaderAction):
    icon = "search"
    iconpos = "notext"
    label = _(u"Search")

    @property
    def href(self):
        plone_portal_state = component.getMultiAdapter(
            (self.context, self.request),
            name="plone_portal_state"
        )
        return plone_portal_state.navigation_root_url() + '/@@search'


class GlobalSections(GlobalSectionsViewlet):
    index = ViewPageTemplateFile("templates/sections.pt")

    def update(self):
        """JQueryMobile select don't fire change event for the already
        selected tab. To fix this behavior and let the user being able to
        qui @@search, controlpanel and other screens, we just include a new
        entry in the portal_tabs with the current view name

        It is a workaround...
        """

        ViewletBase.update(self)  # to add portal_state
        super(GlobalSections, self).update()
        if self.selected_tabs['portal'] == 'index_html':
            #verify we are on the home page.
            #else insert a new entry in portal_tabs
            portal = self.portal_state.portal()
            portal_url = portal.absolute_url()
            default_page = portal.getDefaultPage()
            if default_page:
                default_page = getattr(portal, default_page)
                layout = default_page.getLayout()
                portal_url = default_page.absolute_url() + '/' + layout
            url = self.request['URL']
            if url != portal_url:
                self.selected_tabs['portal'] = 'current'
                info = {
                    'category': 'portal_tabs',
                    'available': True,
                    'description': u'',
                    'title': unicode(url.split('/')[-1]),
                    'url': url,
                    'name': unicode(url.split('/')[-1]),
                    'visible': True,
                    'allowed': True,
                    'link_target': None,
                    'id': 'current',
                    'icon': ''
                }
                self.portal_tabs.insert(0, info)
                self.selected_portal_tab = 'current'
