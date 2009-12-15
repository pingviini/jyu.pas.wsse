from zope.i18nmessageid import MessageFactory
import install

_ = MessageFactory('jyu.pas.wsse')

install.register_wsse_plugin()

def initialize(context):
    """Initializer called when used as a Zope 2 product."""

    install.register_wsse_plugin_class(context)
