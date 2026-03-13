# Step 2/3 - Lesson: write a reusable SSH alias

## Task summary
- Create `out/.ssh/config`
- Write alias `train-node` with its connection info

## What you are learning
Without SSH config, you have to type a long command every time.
SSH config lets you bundle connection settings under one alias.

## Core concepts
### 1) What `Host` means
`Host` is your alias.
It is not the real address.

### 2) The 4 key fields in this step
- `HostName` — real host address
- `User` — login user
- `Port` — login port
- `IdentityFile` — which private key to use

## Your task
Write an SSH config block so that:
- alias is `train-node`
- host is `127.0.0.1`
- user is `trainee`
- port is `2222`
- the key points to the private key from this stage

## Self-check
Read `out/.ssh/config` and confirm:
- the alias is correct
- the fields and values are correct
- the key path is correct

Then run:
```bash
./quest submit
```
