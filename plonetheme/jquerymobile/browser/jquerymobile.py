from zope import component
from zope import interface
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from plonetheme.jquerymobile import interfaces


class JQueryMobile(BrowserView):
    """Default browserview"""
    interface.implements(interfaces.IJqueryMobileView)

    def __init__(self, context, request):
        self.context = context
        self.request = request
        self.dependencies = {}
        self.render = None

    def __call__(self):
        self.update()
        if self.render:
            return self.render
        return self.index()

    def update(self):
        #check default page
        default_page_id = self.context.getDefaultPage()
        if default_page_id:
            default_page = self.context.restrictedTraverse(default_page_id)
            if default_page:
                render = default_page.restrictedTraverse('jquerymobile_view')()
                self.render = render

        self.add_view_dependency(u'plone_portal_state')
        self.add_view_dependency(u'plone_context_state')
        self.add_view_dependency(u'plone')

    def add_view_dependency(self, name):
        self.dependencies[name] = component.getMultiAdapter(
            (self.context, self.request), name=name
        )

    def pageid(self):
        return '-'.join(self.context.getPhysicalPath())[1:]

    def site_title(self):
        pstate = self.dependencies['plone_portal_state']
        return pstate.portal_title()

    def has_left_portlets(self):
        return self.dependencies['plone'].have_portlets(
            'plone.leftcolumn', self.context
        )

    def has_right_portlets(self):
        return self.dependencies['plone'].have_portlets(
            'plone.rightcolumn', self.context
        )

    def has_both_portlets(self):
        return self.has_left_portlets() and self.has_right_portlets()


class PloneSite(JQueryMobile):
    pass


class Document(JQueryMobile):
    index = ViewPageTemplateFile("document.pt")


class Folder(JQueryMobile):
    """Specific version for listing"""
    content_template = ViewPageTemplateFile('content_folder.pt')

    def content(self):
        return self.content_template(self)

    def item_href(self, item_type, use_view_action, item_url):
        if item_type in use_view_action:
            return item_url + '/view'
        return item_url


class Topic(Folder):
    """Specific version for topic"""
