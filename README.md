# CPSC 481 Project 1: Bayesian Network Diagnostics

Diagnose TB, Cancer, or Bronchitis from any combination of symptoms using the
Asia Bayesian network, built with AIMA's `BayesNet` and queried with
`enumeration_ask` (see `aima/probability.py`). The deliverable is the `Diagnostics`
class in `diagnostics.py`.

The AIMA files live in `aima/` because they import each other as `aima.*`,
and the Canvas skeleton imports `aima.probability`.

## Setup

```
pip install numpy ipython
```

## Run

```
python -m unittest -v        # tests
python diagnostics_gui.py    # GUI
```

## Ownership

| Person | Disease    | Nodes              | Input conversion           |
|--------|------------|--------------------|----------------------------|
| 1      | TB         | Asia, TB, TBorC    | `visit_to_asia`            |
| 2      | Cancer     | Smoking, Cancer, Xray | `smoking`, `xray_result` |
| 3      | Bronchitis | Bronchitis, Dyspnea | `dyspnea`                  |

`diagnose()` itself (evidence dict, `enumeration_ask`, picking the max) is shared,
so do it together once the CPTs and conversions are in.

## Workflow

1. Branch off `main`: `tb`, `cancer`, or `bronchitis`.
2. Edit only the lines marked with your name (`# OWNER: Person N` / `TODO (Person N)`)
   in `diagnostics.py`, and your section of `test_diagnostics.py`.
3. Open a PR to `main`.

**Rule:** don't rename nodes or reorder the node list in `Diagnostics.__init__`.
