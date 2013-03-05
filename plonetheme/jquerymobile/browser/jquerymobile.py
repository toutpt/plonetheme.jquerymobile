from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plonetheme.jquerymobile import interfaces
from zope import interface


class JQueryMobile(BrowserView):
    """Default browserview"""
    interface.implements(interfaces.IJqueryMobileView)

    def __call__(self):
        self.update()
        return self.index()

    def update(self):
        pass

    def pageid(self):
        return '-'.join(self.context.getPhysicalPath())[1:]


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
