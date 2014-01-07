import itertools
import sys

if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest

from infi.dtypes.wwn import WWN

class WWNTest(unittest.TestCase):
    def test__acceptable_forms(self):
        raw_forms = [
            '0x1122334455667788',
            '11:22:33:44:55:66:77:88',
            '11-22-33-44-55-66-77-88',
            ]
        forms = [WWN(f) for f in raw_forms]
        for f in forms:
            self.assertEqual(str(f), '1122334455667788')
            self.assertNotEqual(f, '1212121212121212')
            self.assertNotEqual(f, WWN('1212121212121212'))
            for raw in raw_forms:
                self.assertEquals(f, raw)
            for other in forms:
                self.assertEquals(f, other)
            self.assertEqual(f, f)
            self.assertEqual(hash(f), hash(str(f)))
    def test__padding(self):
        self.assertEquals(WWN('1'), '0000000000000001')
    def test__invalid_forms(self):
        for form in ['blap', '', '0x0x', '00::00']:
            with self.assertRaises(ValueError):
                WWN(form)
    def test__initializing_one_fc_address_with_another(self):
        a = WWN(WWN('0x12'))
        self.assertEquals(a, '0x12')
    def test__ordering(self):
        # required for stuff like assertItemsEqual...
        forms = ['12132', '2', '3943', '222222']
        addresses = map(WWN, forms)
        self.assertEqual(sorted(addresses), sorted(x.rjust(16, '0') for x in forms))
        a = WWN('123')
        self.assertTrue(a > '12')
        self.assertFalse(a > '1234')
        self.assertTrue(a >= '12')
        self.assertFalse(a >= '1234')
        self.assertTrue(a <= '123')
        self.assertFalse(a <= '12')

    def test_higher_addresses(self):
        wwn = "ab:cd:ef:FE:DC:BA:01:23"
        self.assertEqual(WWN(wwn), wwn)

    def test_not_equals__empty_string(self):
        wwn = "ab:cd:ef:FE:DC:BA:01:23"
        self.assertNotEqual(WWN(wwn), "")

