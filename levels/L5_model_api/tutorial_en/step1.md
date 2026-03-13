# Step 1/2 - Lesson: patch the example client so it supports two provider formats

## Task summary
- Modify `lab/api_client.py`
- Make the OpenAI-style call succeed
- Make the Anthropic-style call succeed too

## What you are learning
This stage does not ask you to build an API client from scratch.
The repository already gives you one:
- `lab/api_client.py`

Your job is to read it and patch the wrong parts.

## Core concepts
### 1) What the example already does for you
It already handles:
- sending POST requests
- JSON serialization
- reading the response body

So the task is not about network boilerplate.
It is about understanding:
- which URL is correct
- which headers are correct
- which response field is correct

### 2) How the two API styles differ
OpenAI style typically reads text from:
- `choices[0].message.content`

Anthropic style typically reads text from:
- `content[0].text`

The request headers also differ.

## Your task
Patch `lab/api_client.py` so these two functions both work:
- `call_openai_once()`
- `call_anthropic_once()`

The backend will validate requests automatically.
You do not need to create extra output files.

## Self-check
Only run the step-1 runner:
```bash
python lab/run_step1.py
```

Confirm that both calls return text instead of failing because of wrong headers or wrong response parsing.

Then run:
```bash
./quest submit
```
