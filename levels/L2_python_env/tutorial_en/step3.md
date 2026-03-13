# Step 3/3 - Lesson: freeze the environment

## Task summary
- Export the current environment into `out/pip_freeze.txt`
- Confirm that key dependencies appear in the file

## What you are learning
A common problem in Python work is:
“it works on my machine, but not on yours.”

`pip freeze` creates a snapshot of the current environment.

## Core concepts
### 1) What `pip freeze` gives you
A list of installed packages and their exact versions.

### 2) Why activation matters here
You must run it inside the correct virtual environment.
Otherwise you freeze the wrong environment, which makes the snapshot useless.

## Your task
Export the active environment into:
- `out/pip_freeze.txt`

## Self-check
Use commands like `head` or `grep` to confirm key dependencies are present.

Then run:
```bash
./quest submit
```
