import snmpFunctions
import unittest

class TestCalc(unittest.TestCase):
    
    def test_set_get(self):
        value = "hostname"
        snmpFunctions.get("localhost", "public", ".1.3.6.1.2.1.1.5.0")
        snmpFunctions.set("localhost", "public", ".1.3.6.1.2.1.1.5.0", value)
        result = snmpFunctions.get("localhost", "public", ".1.3.6.1.2.1.1.5.0")
        self.assertEqual(str(result), value)

        
if __name__ == "__main__":
    unittest.main()