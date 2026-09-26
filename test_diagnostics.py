import unittest

from diagnostics import Diagnostics


class TestNetworkBuilds(unittest.TestCase):
    """Sanity check that the network can be constructed at all."""

    def test_constructs_without_error(self):
        Diagnostics()


class TestKnownCase(unittest.TestCase):
    """The scenario from the project spec with a known answer.

    Expected to FAIL until every owner has filled in their real
    probabilities (diagnose() currently raises NotImplementedError).
    """

    def test_known_case_returns_cancer(self):
        d = Diagnostics()
        disease, probability = d.diagnose("No", "Yes", "Abnormal", "Absent")
        self.assertEqual(disease, "Cancer")
        self.assertAlmostEqual(probability, 0.4367, places=4)


# ---------------------------------------------------------------------------
# Person 1 (TB): Asia, TB, TBorC
# ---------------------------------------------------------------------------
class TestPerson1TB(unittest.TestCase):

    @unittest.skip("TODO: Person 1")
    def test_visit_to_asia_favors_tb(self):
        # Suggestion: visit_to_asia="Yes", smoking="No", xray_result="Abnormal",
        # dyspnea="NA" should make TB the most likely disease.
        d = Diagnostics()
        disease, probability = d.diagnose("Yes", "No", "Abnormal", "NA")
        self.assertEqual(disease, "TB")


# ---------------------------------------------------------------------------
# Person 2 (Cancer): Smoking, Cancer, Xray
# ---------------------------------------------------------------------------
class TestPerson2Cancer(unittest.TestCase):

    def test_smoking_input_conversion(self):
        from diagnostics import _convert_smoking

        self.assertIs(_convert_smoking("Yes"), True)
        self.assertIs(_convert_smoking("No"), False)
        self.assertIsNone(_convert_smoking("NA"))
        with self.assertRaises(ValueError):
            _convert_smoking("Sometimes")

    def test_xray_input_conversion(self):
        from diagnostics import _convert_xray

        self.assertIs(_convert_xray("Abnormal"), True)
        self.assertIs(_convert_xray("Normal"), False)
        self.assertIsNone(_convert_xray("NA"))
        with self.assertRaises(ValueError):
            _convert_xray("Blurry")

    def test_cancer_nodes_match_network_diagram(self):
        d = Diagnostics()
        smoking = d.net.variable_node("Smoking")
        cancer = d.net.variable_node("Cancer")
        xray = d.net.variable_node("Xray")

        self.assertEqual(smoking.p(True, {}), 0.5)
        self.assertEqual(cancer.p(True, {"Smoking": True}), 0.1)
        self.assertEqual(cancer.p(True, {"Smoking": False}), 0.01)
        self.assertEqual(xray.p(True, {"TBorC": True}), 0.99)
        self.assertEqual(xray.p(True, {"TBorC": False}), 0.05)


# ---------------------------------------------------------------------------
# Person 3 (Bronchitis): Bronchitis, Dyspnea
# ---------------------------------------------------------------------------
class TestPerson3Bronchitis(unittest.TestCase):

    @unittest.skip("TODO: Person 3")
    def test_smoking_and_dyspnea_favors_bronchitis(self):
        # Suggestion: visit_to_asia="No", smoking="Yes", xray_result="Normal",
        # dyspnea="Present" should make Bronchitis the most likely disease.
        d = Diagnostics()
        disease, probability = d.diagnose("No", "Yes", "Normal", "Present")
        self.assertEqual(disease, "Bronchitis")


if __name__ == "__main__":
    unittest.main()
