# Scrape the Web with entities extraction using OpenAI Function

## What is this?

This codebase allows you to scrape any website and extract relevant data points easily.
Create a schema in `schemas.py`, pick a url, and use them with `scrape_with_playwright()` in `main.py` to start scraping.

Tip: each website has the bulk of content either in <p>, <span> or <h> tags. For best performance, choose a combination of tags that work for you.

```python
asyncio.run(scrape_with_playwright(
        url="https://www.bbc.com",
        tags=["span"],
        schema_pydantic=SchemaNewsWebsites
    ))
```

## Setup

### Create a new Python virtual environment

`python -m venv virtual-env` or `python3 -m venv virtual-env` (Mac)

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

```bash
python main.py
```

## Additional Information

- Add onto this a FastAPI server to serve this as an API endpoint for ease of use.

- Use caution when scraping. Don't do anything I wouldn't do (illegal)
