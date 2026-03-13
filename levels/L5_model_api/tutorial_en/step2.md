# Step 2/2 - Lesson: extend the same client with multi-turn, image input, and streaming

## Task summary
- Keep modifying `lab/api_client.py`
- Patch multi-turn messages
- Patch image input structure
- Patch streaming support

## What you are learning
The harder part of model APIs is usually not the first single-turn call.
It is everything that comes after that:
- multi-turn context
- image input structure
- streaming output

This step still uses the same example file.
You are extending it, not rewriting it.

## Core concepts
### 1) Multi-turn is not automatic memory
You keep the conversation alive by sending multiple messages in the request body.

### 2) Image input is a structured message field
You are not uploading a real image file here.
You only need to patch the correct message structure.

### 3) Streaming is not one full JSON response
With streaming, data arrives in chunks.
So code that assumes “read once, parse one JSON object” is no longer enough.

## Your task
Patch `lab/api_client.py` so these three functions work correctly:
- `call_openai_multiturn()`
- `call_openai_image()`
- `call_openai_stream()`

The backend will automatically validate whether these requests were really sent in the right form.

## Self-check
Only run the step-2 runner:
```bash
python lab/run_step2.py
```

Make sure:
- the multi-turn call sends actual history
- the image call no longer sends plain text only
- the streaming call no longer assumes one full JSON body

Then run:
```bash
./quest submit
```
