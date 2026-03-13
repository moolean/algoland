# Step 2/3 - Lesson: install deps, patch config, and run the script

## Task summary
- Install `lab/requirements.txt`
- Copy and fix `out/hparams.yaml`, changing `threshold` to `0.85`
- Run evaluation and produce `out/eval_result.json`

## What you are learning
A very common workflow:
- is the environment ready?
- are dependencies installed?
- is the config correct?
- does the script actually run?

## Core concepts
### 1) `pip install -r ...`
Install all packages listed in a requirements file.

### 2) Config changes affect results
This task is not random trial-and-error.
You are meant to notice that one config field is wrong and patch it deliberately.

### 3) Run first, then verify
Do not stop at “the command finished”.
You still need to inspect the output file.

## Your task
- install dependencies from `lab/requirements.txt`
- copy `lab/hparams_bad.yaml` to `out/hparams.yaml`
- change `threshold` to `0.85`
- run the evaluation script
- generate `out/eval_result.json`

## Self-check
Check the result file and confirm:
- `threshold` is `0.85`
- `status` is `PASS`

Then run:
```bash
./quest submit
```
