# -*- coding: utf-8 -*-

from zope.component import getUtility
from zope.interface import implements

from plone.fieldsets.fieldsets import FormFields
from plone.app.controlpanel.form import ControlPanelForm
from jyu.pas.wsse import _
from jyu.pas.wsse.interface import IWsseControlPanel
from jyu.pas.wsse.interface import IWsseConfiguration
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

class WsseControlPanel(ControlPanelForm):
    """ Pathkey control panel """
    implements(IWsseControlPanel)
    template = ViewPageTemplateFile('control-panel.pt')
    form_fields = FormFields(IWsseConfiguration)

    form_name = _(u"WSSE API Key")
    label = _(u"WSSE API Key")
    description = _(u"Set or modify the WSSE API Key")