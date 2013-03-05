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

        portal_state = component.getMultiAdapter(
            (self.context, self.request), name=u'plone_portal_state'
        )
        context_state = component.getMultiAdapter(
            (self.context, self.request), name=u'plone_context_state'
        )
        self.dependencies['portal_state'] = portal_state
        self.dependencies['context_state'] = context_state

    def pageid(self):
        return '-'.join(self.context.getPhysicalPath())[1:]

    def site_title(self):
        pstate = self.dependencies['portal_state']
        return pstate.portal_title()


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
