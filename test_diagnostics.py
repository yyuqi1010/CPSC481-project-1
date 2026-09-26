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

    @unittest.skip("TODO: Person 2")
    def test_smoking_and_abnormal_xray_favors_cancer(self):
        # Suggestion: visit_to_asia="No", smoking="Yes", xray_result="Abnormal",
        # dyspnea="NA" should make Cancer the most likely disease.
        d = Diagnostics()
        disease, probability = d.diagnose("No", "Yes", "Abnormal", "NA")
        self.assertEqual(disease, "Cancer")


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
