# Step 2/3 - Lesson: fix the JSONL scoring logic so filtering and averaging use the same scope

## Task summary
- Copy `lab/pdb_bug.py` to `out/pdb_bug_fixed.py`
- Fix it so the script outputs `result=4.0`
- Write the run result to `out/run_output.txt`

## What you are learning
After inspecting the failure, the next step is to patch the existing script.
This is a common offline-analysis bug:
- the code filters rows correctly
- but averages using the wrong denominator

## Core concepts
### 1) This is a data-analysis bug, not a toy math bug
The structure is realistic:
- load rows
- filter rows
- aggregate score
- print a final result

The bug is that the selected rows and the averaging scope do not match.

### 2) Patch the existing script instead of rewriting it
The goal is to understand the existing logic and correct the minimal broken part.

## Your task
- copy the original script
- patch the scoring logic
- run the fixed script
- write the result to `out/run_output.txt`

## Self-check
Run:
```bash
python out/pdb_bug_fixed.py
cat out/run_output.txt
```

The final output must include:
- `result=4.0`

Then run:
```bash
./quest submit
```
