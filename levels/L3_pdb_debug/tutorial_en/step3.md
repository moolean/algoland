# Step 3/3 - Lesson: fix the JSONL experiment summary so it chooses the real best run

## Task summary
- Copy `lab/batch_report_bug.py` to `out/batch_report_fixed.py`
- Fix it so the script prints the correct best experiment
- Write the result to `out/final_report.txt`

## What you are learning
In real ML work, the model is not always the problem.
Sometimes the reporting script is wrong.

This task simulates exactly that:
- experiment results are already stored in JSONL
- loading works
- but the “best run” selection logic is wrong

## Core concepts
### 1) What this script does
It:
- reads `experiment_results.jsonl`
- parses each row
- selects the best experiment
- prints a final report

### 2) Why this bug matters
If the best-run logic is reversed, your report can promote the worst run as the best one.
That is a very real analysis mistake.

## Your task
- copy `lab/batch_report_bug.py`
- patch the best-run selection logic
- run the fixed script
- write the result to `out/final_report.txt`

## Self-check
Run:
```bash
python out/batch_report_fixed.py
cat out/final_report.txt
```

The final result should clearly show:
- `best=run_a`
- `val_score=0.873`

Then run:
```bash
./quest submit
```
