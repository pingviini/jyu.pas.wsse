from Testing import ZopeTestCase as ztc
from Products.PloneTestCase.layer import PloneSite
from Products.Five import zcml
from Products.Five import fiveconfigure
import jyu.pas.wsse

class WSSELayer(PloneSite):

    @classmethod
    def setUp(cls):
        fiveconfigure.debug_mode = True
        zcml.load_config('configure.zcml',
                         jyu.pas.wsse)
        ztc.installPackage('jyu.pas.wsse')
        ztc.installPackage('jyu.m3.atom')
        fiveconfigure.debug_mode = False
        pass

    @classmethod
    def tearDown(cls):
        pass
