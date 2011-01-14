from zope.i18nmessageid import MessageFactory

messageFactory = MessageFactory("plonetheme.jquerymobile")

_ = messageFactory

label_domains = _(u"label_domains",
                  default=u"Domains")

desc_domains =   _(u"desc_domains",
                   default=u"Domains for which mobile themes will be use. One per line")

label_controlpanel = _(u"label_controlpanel",
                       default=u"Jquery Mobile theme settings")

