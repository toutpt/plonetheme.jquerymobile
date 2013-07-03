from plone.app.layout.viewlets import common
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils import getToolByName


class PanelLeftHeader(common.ViewletBase):
    weight = 0


class PanelRightHeader(common.ViewletBase):
    pass


class UserToolBar(common.ContentActionsViewlet, common.ContentViewsViewlet):
    """add content"""

    index = ViewPageTemplateFile('templates/usertoolbar.pt')
    weight = 10
    def update(self):
        common.ContentActionsViewlet.update(self)
        common.ContentViewsViewlet.update(self)
        self.portal_types = getToolByName(self.context, 'portal_types')
        if self.context.portal_type in ("collective.rcse.group", "Plone Site"):
            self.container = self.context
        else:
            self.container = self.context.aq_inner.aq_parent
        self.filters = []
        self.current_filter = None
        if self.request.get('filter', False):
            self.current_filter = self.request.get('portal_type', None)

    def get_filters(self):
        if not self.filters:
            types = self.container.allowedContentTypes()
            for fti in types:
                context_url = self.context.absolute_url()
                url = '%s?filter=1&portal_type=%s' % (context_url, fti.id)
                info = {"url": url, "id": fti.id, "title": fti.Title()}
                info["current"] = False
                if fti.id == self.current_filter:
                    info["current"] = True
                self.filters.append(info)
        return self.filters


class RightPanel(common.ViewletBase):
    def render(self):
        plone_view = self.context.restrictedTraverse('@@plone')
        if plone_view.have_portlets('plone.rightcolumn', self.context):
            return self.index()
        return ""
