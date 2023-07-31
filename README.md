# Scrape the Web with entities extraction using OpenAI Function

## What is this?

This codebase allows you to scrape any website and extract relevant data points easily.

Add onto this a FastAPI server to serve this as an API endpoint for ease of use.

## Setup

### Create a new Python virtual environment

`python -m venv virtual-env` (Mac)

`py -m venv virtual-env` (Windows 11)

### Activate virtual environment

`.\virtual-env\Scripts\activate` (Windows)

`source virtual-env/bin/activate` (Mac)

### Install dependencies

Run `poetry install --sync` or `poetry install`

### Install playwright (for SPAs or JS-heavy websites that require a browser to be opened)

```bash
playwright install
```

### Create a new `.env` file

```text
OPENAI_API_KEY=XXXXXX
```

## Usage

### Run locally

python main.py

## Additional Information

Some sites don't allow scraping

- Bestbuy
- Amazon
