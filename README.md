# Switchgear Application Engineering — Demonstration Work Samples

Three **newly authored illustrative samples**, not past client work or stamped engineering designs. Prepared as a portfolio demonstration for an OEM switchgear application engineering role. All ratings, prices and equipment assumptions are fictional examples and require OEM confirmation and qualified engineering review.

## Samples
1. [Technical proposal and specification review](proposal/lv-switchgear-proposal.md): requirements, exclusions, RFIs, quotation framework.
2. [Budgetary switchgear estimator](calculator/estimate.py): executable Python CLI, sample input and reproducible tests.
3. [Customer presentation and voiceover script](customer-presentation/walkthrough-script.md): a narrated 5-slide technical walkthrough.

## Run calculator
Requires Python 3.10+; no external packages.

```bash
python calculator/estimate.py calculator/sample-request.json
python -m unittest discover -s tests -v
```

**Important:** The estimator is for illustration only. It is not an electrical design tool, a protective-device coordination study, an arc-flash assessment, a binding quotation, or a substitute for NEC/NFPA/IEEE/UL requirements and OEM approvals.
