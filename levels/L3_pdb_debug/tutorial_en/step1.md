# Step 1/3 - Lesson: use PDB to inspect why a JSONL scoring script is wrong

## Task summary
- Record a PDB session into `out/pdb_session.txt`
- Debug `lab/pdb_bug.py`
- Inspect the filtered rows and whether the denominator is reasonable

## What you are learning
PDB is not about memorizing commands.
It is about stopping the program at the right place and inspecting the real execution state.

This task uses a more algorithm-flavored script:
- load rows from JSONL
- filter rows
- aggregate scores
- produce a final score

## Core concepts
### 1) `python -m pdb lab/pdb_bug.py`
This runs the script under PDB instead of running it normally.
After entering PDB, the program is paused and waiting for debug commands.

### 2) Why `c` alone can run too far
`c` means continue.
Without a breakpoint, it may run all the way to the end.
So if you want to inspect `selected`, you must first stop inside `build_score()`.

### 3) Useful commands here
- `l` — list current code
- `b build_score` — set a breakpoint at the function entry
- `c` — continue until a breakpoint or the end
- `n` — execute the next line in the current frame
- `p selected` — inspect filtered rows
- `p len(selected)` — inspect the filtered row count
- `q` — quit

### 4) How to record the session
Use:
```bash
script -q -F -k out/pdb_session.txt python -m pdb lab/pdb_bug.py
```

## Your task
Run one full PDB session and record it into:
- `out/pdb_session.txt`

## Self-check
The recording should clearly show:
- `(Pdb)`
- `b build_score`
- `selected`
- `len(selected)`

Then run:
```bash
./quest submit
```
