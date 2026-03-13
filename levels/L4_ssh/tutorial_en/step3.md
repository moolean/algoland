# Step 3/3 - Lesson: use the alias for a simulated SSH login

## Task summary
- Use `train-node` to complete one simulated login
- Write the login result to `out/login_result.txt`

## What you are learning
After generating keys and writing config, the next step is to actually use the alias.

In real work, you would not keep rereading the config file.
You would use the alias directly.

## Core concepts
### 1) Why `ssh train-node` can work
Because the config already tells SSH which host, user, port, and key belong to `train-node`.

### 2) Why this stage uses a simulated login
There is no real SSH server here.
Instead, the stage provides a script that checks whether your config is good enough for a correct alias-based login.

## Your task
Use the provided script:
- `lab/mock_ssh_login.sh`

Complete one simulated login with the alias `train-node` and write the result to:
- `out/login_result.txt`

## Self-check
Read `out/login_result.txt`.
If everything is correct, it should contain:
- `login ok`
- `alias=train-node`

Then run:
```bash
./quest submit
```
