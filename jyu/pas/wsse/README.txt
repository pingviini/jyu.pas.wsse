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


We have WSSE plugin added so now we start testing if it works.
First we change news folder to private and then log off our admin
user.
	
	>>> portal_url = self.portal.absolute_url()
	>>> browser.open(portal_url + '/news')
	>>> browser.getLink('Advanced...').click()
    >>> browser.getControl(name='workflow_action').getControl(value='retract').selected = True
    >>> browser.getControl('Save').click()
    >>> browser.contents
    '...status...private...'

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/news/atombrowser')
	>>> browser.contents
	'...Log in...'

TODO: Need to add test user

Now we add WSSE Headers

	>>> browser.addHeader('Authorization', 'WSSE profile="UsernameToken"')
	>>> browser.addHeader('X-WSSE', 'UsernameToken Username="wsseuser", PasswordDigest="quR/EWLAV4xLf9Zqyw4pDmfV9OY=", Nonce="d36e316282959a9ed4c89851497a717f", Created="2003-12-15T14:43:07Z")

	>>> interact(locals())

    >>> 'ALL OK'
    'ALL OK'
