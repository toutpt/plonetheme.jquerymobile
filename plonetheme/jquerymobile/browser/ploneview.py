from Products.CMFPlone.browser import ploneview as base
from Products.CMFPlone.browser.interfaces import IPlone
from plone.i18n.normalizer.interfaces import IIDNormalizer
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.browserpage.viewpagetemplatefile import (
    ViewPageTemplateFile as ZopeViewPageTemplateFile
)
from plone.uuid.interfaces import IUUID
from zope.component import queryAdapter, queryUtility


class IPloneView(IPlone):
    def getPageId(template, view):
        """Return a page id for jquerymobile"""


class PloneView(base.Plone):
    def getPageId(self, template, view):
        pageid = ''

        uid = queryAdapter(self.context, IUUID)
        if uid:
            pageid += str(uid)

        if isinstance(template, ViewPageTemplateFile) or \
           isinstance(template, ZopeViewPageTemplateFile):
            # Browser view
            pageid += view.__name__
        else:
            pageid += template.getId()

        #batch support
        b_start = self.request.get('b_start', None)
        if b_start is not None:
            pageid += "-bstart-%s" % b_start

        normalizer = queryUtility(IIDNormalizer)
        pageid = normalizer.normalize(pageid)

        return pageid
