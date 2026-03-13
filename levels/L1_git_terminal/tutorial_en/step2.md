# Step 2/4 - Lesson: extract -> count -> sort

## Task summary
- Find the top 2 most frequent error types in `lab/train.err.log`
- Write them as `<error_type> <count>` into `out/error_top2.txt`

## What you are learning
This is one of the most common shell data-processing patterns:
1. extract the part you care about
2. group identical values together
3. count them
4. sort them
5. keep the top few

## Core concepts
### 1) Why `sort` comes before `uniq -c`
`uniq -c` only counts consecutive repeated values.
So identical values must be grouped together first.
That is why `sort` comes before `uniq -c`.

### 2) Why there are two different sorts
- one sort groups equal values together
- another sort ranks results by frequency

### 3) Why `head -n 2`
After counting and sorting by frequency, you only keep the top 2.

## Your task
Count the most frequent error types in:
- `lab/train.err.log`

Write the top 2 to:
- `out/error_top2.txt`

Required format:
```text
<error_type> <count>
```

## Self-check
The file should:
- have 2 lines
- be sorted by count descending
- use the format `error_type count`

Then run:
```bash
./quest submit
```
