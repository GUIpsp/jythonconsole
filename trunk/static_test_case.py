import unittest
import jintrospect

class StaticTestCase(unittest.TestCase):

    def setUp(self):
        pass
        
    def testStaticAutoComplete(self):
        from java.util.logging import Level
        list = jintrospect.getAutoCompleteList("Level.", locals())
        self.assertEquals(10, len(list))
        self.assert_(list.index("INFO") > -1)
        
    def testStaticPropertyFromAncestor(self):
        from javax.swing import JButton
        list = jintrospect.getAutoCompleteList("JButton.", locals())
        self.assert_(len(list) > 0)
        self.assert_(list.index("TEXT_CHANGED_PROPERTY") > -1)

    def testStaticMethodFromAncestor(self):
        from javax.swing.border import EtchedBorder
        list = jintrospect.getAutoCompleteList("EtchedBorder.", locals())
        print list
        self.assert_(len(list) > 0)
        self.assert_(list.index("getInteriorRectangle") > -1)

if __name__ == '__main__':
    unittest.main()
