# Step 2/2 - Lesson: your first real edit in Vim

## Task summary
- Create `out/hello_vim.txt`
- The file must have at least 2 lines and include the word `vim`

## What you are learning
Vim is different from most GUI editors.
You do not open it and immediately start typing.

The most important thing to learn first is that Vim has modes.

## Core concepts
### 1) Normal mode
When Vim opens, it starts in normal mode.
In this mode, keys are interpreted as commands.

### 2) Insert mode
Press `i` to enter insert mode.
Only in insert mode do your letters become file content.

### 3) Saving and leaving
- `Esc` returns to normal mode
- `:wq` means write + quit
- `:q!` means quit without saving

## Your task
Create a new file:
- `out/hello_vim.txt`

It must:
- contain at least 2 lines
- include the word `vim`

## Self-check
Run:
```bash
cat out/hello_vim.txt
```

Then confirm:
- it has at least 2 lines
- one of the lines contains `vim`

Then run:
```bash
./quest submit
```
