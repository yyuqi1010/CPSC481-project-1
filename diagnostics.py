"""
Diagnostics: Bayesian network that diagnoses TB, Cancer, or Bronchitis
from (possibly partial) symptom evidence, using AIMA's BayesNet and
enumeration_ask.
"""

from aima.probability import BayesNet, enumeration_ask, T, F


def _convert_asia(value):
    """Convert visit_to_asia ("Yes"/"No"/"NA") to True/False/None.

    Returns True, False, or None (None means the value was "NA", i.e.
    unknown, and must be left out of the evidence dict).
    """
    values = {"Yes": T, "No": F, "NA": None}
    try:
        return values[value]
    except KeyError as error:
        raise ValueError(
            "visit_to_asia must be 'Yes', 'No', or 'NA'"
        ) from error


def _convert_smoking(value):
    """Convert smoking ("Yes"/"No"/"NA") to True/False/None."""
    values = {"Yes": T, "No": F, "NA": None}
    try:
        return values[value]
    except KeyError as error:
        raise ValueError("smoking must be 'Yes', 'No', or 'NA'") from error


def _convert_xray(value):
    """Convert xray_result ("Abnormal"/"Normal"/"NA") to True/False/None."""
    values = {"Abnormal": T, "Normal": F, "NA": None}
    try:
        return values[value]
    except KeyError as error:
        raise ValueError(
            "xray_result must be 'Abnormal', 'Normal', or 'NA'"
        ) from error


def _convert_dyspnea(value):
    """Convert dyspnea ("Present"/"Absent"/"NA") to True/False/None."""
    if value == "NA":
        return None
    elif value == "Present":
        return True
    elif value == "Absent":
        return False
    else:
        raise ValueError("dyspnea value must be 'Present', 'Absent', or 'NA'")


class Diagnostics:
    """ Use a Bayesian network to diagnose between three lung diseases """

    def __init__(self):
        # Node list is parent-before-child (required by BayesNet.add).
        # Each CPT value is P(node=True | parents), from the lecture diagram.
        self.net = BayesNet([
            ('Asia', '', 0.01),
            ('Smoking', '', 0.5),
            ('TB', 'Asia', {T: 0.05, F: 0.01}),
            ('Cancer', 'Smoking', {T: 0.1, F: 0.01}),
            ('Bronchitis', 'Smoking', {T: 0.6, F: 0.3}),
            ('TBorC', ['TB', 'Cancer'], {
                (T, T): 1.0, (T, F): 1.0, (F, T): 1.0, (F, F): 0.0,
            }),
            ('Xray', 'TBorC', {T: 0.99, F: 0.05}),
            ('Dyspnea', ['TBorC', 'Bronchitis'], {
                (T, T): 0.9, (T, F): 0.7, (F, T): 0.8, (F, F): 0.1,
            }),
        ])

    def diagnose(self, visit_to_asia, smoking, xray_result, dyspnea):
        """Return [most_likely_disease, probability].

        most_likely_disease is exactly "TB", "Cancer", or "Bronchitis".
        Any argument equal to "NA" is unknown and left out of the evidence.
        """
        observed = {
            'Asia': _convert_asia(visit_to_asia),
            'Smoking': _convert_smoking(smoking),
            'Xray': _convert_xray(xray_result),
            'Dyspnea': _convert_dyspnea(dyspnea),
        }
        evidence = {node: value for node, value in observed.items()
                    if value is not None}

        probabilities = {
            disease: enumeration_ask(disease, evidence, self.net)[T]
            for disease in ('TB', 'Cancer', 'Bronchitis')
        }
        most_likely = max(probabilities, key=probabilities.get)
        return [most_likely, probabilities[most_likely]]
