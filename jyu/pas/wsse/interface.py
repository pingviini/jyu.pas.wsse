from Products.PluggableAuthService import interfaces
from zope.interface import Interface
from zope import schema
from zope.i18nmessageid import MessageFactory
_ = MessageFactory('jyu.pas.wsse')

class IWsseHelper(interfaces.plugins.IExtractionPlugin):
    """interface for WsseHelper."""


class IWsseConfiguration(Interface):
    """ Configuration for WSSE Pas Plugin """

    apiKey = schema.ASCIILine(
        title = _(u"API key"),
        description = _(u"API key for WSSE Authorization"),
        required = True,
    )


class IWsseControlPanel(Interface):
    """ Control panel for Oembed Plone API """


class IWsse(IWsseConfiguration):
    """ WSSE marker """
