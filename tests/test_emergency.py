import unittest

from safety import emergency


class EmergencyDetectionTests(unittest.TestCase):
    def test_category_groups_exist(self):
        self.assertTrue(hasattr(emergency, "CARDIAC"))
        self.assertTrue(hasattr(emergency, "BREATHING"))
        self.assertTrue(hasattr(emergency, "NEURO"))
        self.assertTrue(hasattr(emergency, "BLEEDING"))
        self.assertTrue(hasattr(emergency, "POISON"))

    def test_detects_common_emergency_terms(self):
        self.assertTrue(emergency.is_emergency("I have chest pain"))
        self.assertTrue(emergency.is_emergency("I cannot breathe"))
        self.assertTrue(emergency.is_emergency("I may have taken poison"))


if __name__ == "__main__":
    unittest.main()
