from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plonetheme.jquerymobile import interfaces
from zope import interface


class JQueryMobile(BrowserView):
    """Default browserview"""
    interface.implements(interfaces.IJqueryMobileView)

    def apply_to_context(self):
        """Give a condition to know if the view apply to the context"""
        return False


class Folder(JQueryMobile):
    """Specific version for listing"""
    index = ViewPageTemplateFile('folder.pt')

    def apply_to_context(self):
        return True

    def __call__(self):
        return self.index()

    def item_href(self, item_type, use_view_action, item_url):
        if item_type in use_view_action:
            return item_url + '/view'
        return item_url


class Topic(Folder):
    """Specific version for topic"""
