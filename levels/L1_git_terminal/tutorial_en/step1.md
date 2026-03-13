# Step 1/4 - Lesson: inspect a log first, then use awk to find the best run

## Task summary
- Find the original full line with the smallest `val_loss` in `lab/experiments.log`
- Write that line to `out/best_run.txt`

## What you are learning
Many beginners panic when they see `awk`, but the real problem is usually not awk itself.
It is starting to write commands before understanding the text structure.

## Core concepts
### 1) Read the log structure first
Before you write a command, inspect the file and find:
- what each column means
- which column contains `val_loss=...`

### 2) What `awk` is good for
`awk` is good at processing text by columns.
In awk:
- `$1` means column 1
- `$2` means column 2
- `$3` means column 3

### 3) Why `split()` matters here
If the third column looks like `val_loss=0.214`, you still need to separate the name and the numeric value.
That is where `split()` helps.

## Your task
From:
- `lab/experiments.log`

Find the original line with the smallest `val_loss` and write it to:
- `out/best_run.txt`

## Self-check
The output should:
- contain exactly 1 line
- be the original full line from the log
- correspond to the smallest `val_loss`

Then run:
```bash
./quest submit
```
