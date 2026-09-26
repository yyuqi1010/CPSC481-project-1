"""
Diagnostics: Bayesian network that diagnoses TB, Cancer, or Bronchitis
from (possibly partial) symptom evidence, using AIMA's BayesNet and
enumeration_ask.

GROUP RULE: do not rename any node/variable name below, and do not
reorder the node list in __init__ (BayesNet.add() requires each node's
parents to already be in the network). Only edit the lines marked with
your name.
"""

from aima.probability import BayesNet, enumeration_ask, T, F


# ---------------------------------------------------------------------------
# Person 1 (TB): converts visit_to_asia
# ---------------------------------------------------------------------------
def _convert_asia(value):
    """Convert visit_to_asia ("Yes"/"No"/"NA") to True/False/None.

    Returns True, False, or None (None means the value was "NA", i.e.
    unknown, and must be left out of the evidence dict).
    """
    # TODO (Person 1): implement the conversion.
    raise NotImplementedError


# ---------------------------------------------------------------------------
# Person 2 (Cancer): converts smoking and xray_result
# ---------------------------------------------------------------------------
def _convert_smoking(value):
    """Convert smoking ("Yes"/"No"/"NA") to True/False/None."""
    # TODO (Person 2): implement the conversion.
    raise NotImplementedError


def _convert_xray(value):
    """Convert xray_result ("Abnormal"/"Normal"/"NA") to True/False/None."""
    # TODO (Person 2): implement the conversion.
    raise NotImplementedError


# ---------------------------------------------------------------------------
# Person 3 (Bronchitis): converts dyspnea
# ---------------------------------------------------------------------------
def _convert_dyspnea(value):
    """Convert dyspnea ("Present"/"Absent"/"NA") to True/False/None."""
    # TODO (Person 3): implement the conversion.
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
        # Every CPT below is a 0.5 placeholder - replace with the real
        # numbers from the diagram, keeping the same dict shape.
        self.net = BayesNet([
            # OWNER: Person 1 (TB)  # TODO: fill from diagram
            ('Asia', '', 0.5),

            # OWNER: Person 2 (Cancer)  # TODO: fill from diagram
            ('Smoking', '', 0.5),

            # OWNER: Person 1 (TB)  # TODO: fill from diagram
            ('TB', 'Asia', {T: 0.5, F: 0.5}),

            # OWNER: Person 2 (Cancer)  # TODO: fill from diagram
            ('Cancer', 'Smoking', {T: 0.5, F: 0.5}),

            # OWNER: Person 3 (Bronchitis)  # TODO: fill from diagram
            ('Bronchitis', 'Smoking', {T: 0.6, F: 0.3}),

            # OWNER: Person 1 (TB)  # TODO: fill from diagram
            ('TBorC', ['TB', 'Cancer'], {
                (T, T): 0.5, (T, F): 0.5, (F, T): 0.5, (F, F): 0.5,
            }),

            # OWNER: Person 2 (Cancer)  # TODO: fill from diagram
            ('Xray', 'TBorC', {T: 0.5, F: 0.5}),

            # OWNER: Person 3 (Bronchitis)  # TODO: fill from diagram
            ('Dyspnea', ['TBorC', 'Bronchitis'], {
                (T, T): 0.9, (T, F): 0.7, (F, T): 0.8, (F, F): 0.1,
            }),
        ])

    def diagnose(self, visit_to_asia, smoking, xray_result, dyspnea):
        """Return [most_likely_disease, probability].

        most_likely_disease is exactly "TB", "Cancer", or "Bronchitis".
        Any argument equal to "NA" is unknown and must be left out of
        the evidence passed to enumeration_ask.

        Shared final step - whoever picks this up should coordinate
        with the group rather than editing alone.
        """
        # TODO (all): convert each input with the helpers above
        #   (_convert_asia, _convert_smoking, _convert_xray, _convert_dyspnea).
        # TODO (all): build an evidence dict keyed by node name
        #   (e.g. {'Asia': True, 'Xray': False}), skipping any conversion
        #   that came back None (NA).
        # TODO (all): call enumeration_ask('TB', evidence, self.net), and
        #   likewise for 'Cancer' and 'Bronchitis'. Each call returns a
        #   ProbDist; the probability the disease is present is dist[T].
        # TODO (all): return [name, probability] for whichever of the
        #   three has the highest probability.
        raise NotImplementedError
