Tests for jyu.pas.wsse

test setup
----------

    >>> from Testing.ZopeTestCase import user_password
    >>> from Products.Five.testbrowser import Browser
    >>> browser = Browser()

Plugin setup
------------
	>>> self.setRoles(('Manager',))
	>>> from Products.PloneTestCase import PloneTestCase as ptc
	>>> browser.open('http://nohost/plone/login_form')
	>>> browser.getControl(name='__ac_name').value = ptc.default_user
	>>> browser.getControl(name='__ac_password').value = ptc.default_password
	>>> browser.getControl('Log in').click()
	
    >>> acl_users_url = "%s/acl_users" % self.portal.absolute_url()
    >>> browser.open("%s/manage_main" % acl_users_url)
    >>> browser.url
    'http://nohost/plone/acl_users/manage_main'
    >>> form = browser.getForm(index=0)
    >>> select = form.getControl(name=':action')

jyu.pas.wsse should be in the list of installable plugins:

    >>> 'WSSE Helper' in select.displayOptions
    True

and we can select it:

    >>> select.getControl('WSSE Helper').click()
    >>> select.displayValue
    ['WSSE Helper']
    >>> select.value
    ['manage_addProduct/jyu.pas.wsse/manage_add_wsse_form']

we add 'Wsse Helper' to acl_users:

    >>> from jyu.pas.wsse.plugin import WsseHelper
    >>> myhelper = WsseHelper('myplugin', 'Wsse Helper')
    >>> self.portal.acl_users['myplugin'] = myhelper

and so on. Continue your tests here

    >>> interact(locals())
    >>> 'ALL OK'
    'ALL OK'


