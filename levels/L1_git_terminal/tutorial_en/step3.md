# Step 3/4 - Lesson: copy a config, patch it, and verify it yourself

## Task summary
- Copy `lab/configs/model_bad.yaml` to `out/model_fixed.yaml`
- Change `lr` to `0.001` and `batch_size` to `32`

## What you are learning
A basic engineering habit:
**copy the original config first, then edit the copy.**

This keeps the original intact and makes the change easier to inspect.

## Core concepts
### 1) Why `cp` matters here
You are not editing the source file directly.
You are creating a safe working copy.

### 2) Why self-check matters
Many mistakes are simple:
- wrong file
- forgot to save
- one digit is wrong
- changed the wrong field

So this step is really about careful verification.

## Your task
Copy and patch the config so that:
- `lr: 0.001`
- `batch_size: 32`

Write the fixed version to:
- `out/model_fixed.yaml`

## Self-check
Run:
```bash
cat out/model_fixed.yaml
```

Confirm that both exact values are present.

Then run:
```bash
./quest submit
```
