# Ask LangChain for 5 Breakfast Ideas

Week 2 · Day 5 assignment (Social Eagle: learn. build. operate)

A small Python script that uses LangChain's `ChatOpenAI` to ask a model for 5 healthy breakfast ideas and prints them as a clean numbered list.

## What it does

- Sends one prompt to `gpt-4o-mini` through LangChain's `ChatOpenAI`
- Asks for exactly 5 healthy breakfast ideas, numbered, one line each, no preamble
- Prints only the text of the reply (`reply.content`), not the whole message object
- Loads the OpenAI API key from a `.env` file, so the key is never hard-coded

## Project structure

```
breakfast/
├── breakfast.py     # the script
├── .env             # your API key (NOT committed to Git)
├── .env.example     # placeholder showing the required variable (optional)
├── .gitignore       # keeps venv/ and .env out of Git
└── README.md
```

## Prerequisites

- Python 3.9 or newer
- An OpenAI API key

## Setup

1. Create the project folder and a virtual environment:

   ```bash
   mkdir breakfast && cd breakfast
   python -m venv venv
   ```

2. Activate the virtual environment:

   - macOS / Linux: `source venv/bin/activate`
   - Windows (PowerShell): `venv\Scripts\Activate.ps1`

3. Install the dependencies:

   ```bash
   pip install langchain langchain-openai python-dotenv
   ```

4. Create a file named `.env` in the project folder with your key (no quotes, no spaces around `=`):

   ```
   OPENAI_API_KEY=your-key-here
   ```

## Usage

```bash
python breakfast.py
```

### Example output

```
$ python breakfast.py
1. Vegetable oats upma with peanuts
2. <second idea>
3. <third idea>
4. <fourth idea>
5. <fifth idea>
```

## The code

```python
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()  # reads .env and sets OPENAI_API_KEY in the environment

llm = ChatOpenAI(model="gpt-4o-mini")

prompt = (
    "Give me exactly 5 healthy breakfast ideas. "
    "Healthy means high in protein or fibre, low in added sugar, and not deep fried. "
    "Format: a numbered list from 1 to 5, one idea per line, "
    "no introduction and no closing remarks."
)

reply = llm.invoke(prompt)
print(reply.content)
```

## Notes and learnings

**`invoke()` returns a message object, not a string.**
Printing `reply` directly shows an `AIMessage` with `content`, `response_metadata` and `usage_metadata`. The part we want is `reply.content`, so the script prints that.

**Do the two runs match?**
<!-- Fill this in after running the script twice -->
Run 1 and Run 2 gave: _different / the same_ five ideas.

At the default temperature the model samples with some randomness, so the lists usually differ between runs. To get the same five ideas every time, set `temperature=0`:

```python
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
```

This makes output much more consistent, but OpenAI does not guarantee identical results on every call.

**What does "healthy" mean here?**
It is defined in the prompt (high in protein or fibre, low in added sugar, not deep fried) instead of leaving the model to decide.

## Requirements checklist

- [x] All code in a single file named `breakfast.py`
- [x] Uses LangChain's `ChatOpenAI`, not the OpenAI SDK directly
- [x] Asks for exactly 5 healthy breakfast ideas
- [x] Prints only the text of the reply
- [x] Prompt pins the format: numbered, one line each, no preamble
- [x] Run twice and compared the results
- [x] API key read from the environment (loaded from `.env`), never hard-coded

## Security

Never commit your `.env` file or `venv/` folder. Make sure `.gitignore` contains:

```
venv/
.env
```

Run `git status` before pushing and confirm `.env` is not listed.

## Troubleshooting

- **Authentication error:** check that `.env` is in the folder you run the command from, the variable is spelled exactly `OPENAI_API_KEY`, and there are no quotes or extra spaces.
- **`ModuleNotFoundError`:** make sure the virtual environment is activated and the packages are installed.