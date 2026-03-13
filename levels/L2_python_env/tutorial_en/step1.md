# Step 1/3 - Lesson: why each Python project should have its own environment

## Task summary
- Create a virtual environment in `out/.venv`
- Activate it and confirm your current `python` points to that environment

## What you are learning
Many Python problems are really environment problems:
- package versions conflict across projects
- you think you are using the project environment, but you are using system Python
- packages are installed into the wrong place

`venv` gives the current project an isolated environment.

## Core concepts
### 1) `python3 -m venv <dir>`
This creates a virtual environment in the directory you choose.

### 2) `source <dir>/bin/activate`
This activates the virtual environment in your current shell.
After activation, commands like `python` and `pip` should resolve to that environment.

### 3) Why `which python` matters
Prompt changes are helpful, but `which python` is the real verification.
It tells you exactly which Python executable you are using.

## Your task
Create a virtual environment in:
- `out/.venv`

Activate it and confirm that your current Python comes from that environment.

## Self-check
Run:
```bash
which python
python -V
```

The path should include `.venv`.

Then run:
```bash
./quest submit
```
