from plone.app.layout.viewlets.common import ViewletBase, ContentViewsViewlet
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class JQueryMobileContentViewsViewlet(ContentViewsViewlet):
    index = ViewPageTemplateFile("templates/contentviews.pt")
