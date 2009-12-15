# -*- coding: utf-8 -*-

from zope.interface import implements
from zope.schema.fieldproperty import FieldProperty
from zope.component import getUtility
from zope.interface import classProvides

from jyu.pas.wsse.interface import IWsse
from jyu.pas.wsse.interface import IWsseConfiguration

from OFS.SimpleItem import SimpleItem

    
def form_adapter(context):
    """Form Adapter"""
    return getUtility(IWsse)


class Wsse(SimpleItem):
    """Wsse Utility"""
    implements(IWsse)

    classProvides(
        IWsseConfiguration,
    )

    apiKey = FieldProperty(IWsseConfiguration['apiKey'])
