from Products.PlonePAS.Extensions.Install import activatePluginInterfaces
from Products.CMFCore.utils import getToolByName
from StringIO import StringIO
from install import manage_add_wsse_helper

def importVarius(context):
    ''' Install the ExamplePAS plugin
    '''
    out = StringIO()
    portal = context.getSite()

    uf = getToolByName(portal, 'acl_users')
    installed = uf.objectIds()

    if 'WSSE PAS Plugin' not in installed:
        addExamplePlugin(uf, 'wsse', 'WSSE PAS Plugin')
        activatePluginInterfaces(portal, 'wsse', out)
    else:
        print >> out, 'wsse already installed'

    print out.getvalue()