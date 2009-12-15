from Testing import ZopeTestCase as ztc
from base import TestCase
import interlude
import unittest

def test_suite():
    return unittest.TestSuite([
        ztc.FunctionalDocFileSuite(
            'README.txt', package='jyu.pas.wsse',
            test_class=TestCase,
            globs=dict(interact=interlude.interact,),)
    ])

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
