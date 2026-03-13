# Step 1/3 - Lesson: generate an SSH key pair

## Task summary
- Generate an ed25519 key pair in `out/.ssh/`

## What you are learning
SSH login often uses keys instead of passwords.
For this step, you only need the basic idea:
- keep the private key on your side
- the public key can be shared with the remote machine

## Core concepts
### 1) What `ssh-keygen` does
It generates an SSH key pair.
It does not log in to a machine.

### 2) The key parameters in this task
- `-t ed25519` — key type
- `-f <path>` — output path
- `-N ""` — empty passphrase

### 3) Why `out/.ssh/`
This stage does not touch your real `~/.ssh/`.
Everything stays inside the stage workspace.

## Your task
Create an ed25519 key pair with an empty passphrase under:
- `out/.ssh/`

## Self-check
Confirm that `out/.ssh/` contains:
- `id_ed25519`
- `id_ed25519.pub`

Then run:
```bash
./quest submit
```
