from Products.PloneTestCase import ptc
from jyu.pas.wsse.tests.layer import WSSELayer

ptc.setupPloneSite()


class TestCase(ptc.PloneTestCase):
    '''TestCase for WSSE'''

    layer = WSSELayer
    

class FunctionalTestCase(ptc.FunctionalTestCase):
    '''TestCase for WSSE'''

    layer = WSSELayer