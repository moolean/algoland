# Step 1/2 - Lesson: command output, pipes, and redirection

## Task summary
- Write the first line of the Vim version output to `out/vim_version.txt`
- Figure out how to chain “produce output / keep the first line / write to a file"

## What you are learning
A long terminal command is usually not one big spell.
It is several small parts working together.

In this step, you only need to understand 4 roles:
- something that produces text
- something that keeps only the part you want
- something that passes output forward
- something that writes the final result to a file

## Core concepts
### 1) What is `vim --version`
Vim is a text editor.
But `vim --version` does not open the editor.
It asks the Vim program to print its version information.

So in this task, it is the **source of text output**.

### 2) What is `|`
`|` is a pipe.
It passes the output from the command on the left to the command on the right.

Think of it as a conveyor belt.

### 3) What is `head -n 1`
`head` keeps the first few lines of text.
`head -n 1` means: keep only the first line.

### 4) What is `>`
`>` is shell redirection.
It sends output into a file instead of printing it on screen.

## Small examples
```bash
vim --version
printf "a\nb\nc\n" | head -n 1
echo "demo" > /tmp/demo.txt
```

## Your task
Use these building blocks to write the first line of Vim version info into:
- `out/vim_version.txt`

## Self-check
Run:
```bash
cat out/vim_version.txt
```

If you see text like `VIM` or `Vi IMproved`, you are on the right track.

Then run:
```bash
./quest submit
```
