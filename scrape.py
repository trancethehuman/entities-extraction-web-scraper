import asyncio
import pprint

import requests
from bs4 import BeautifulSoup
from playwright.async_api import async_playwright


def remove_unwanted_tags(html_content, unwanted_tags=["script", "style"]):
    soup = BeautifulSoup(html_content, 'html.parser')

    for tag in unwanted_tags:
        for element in soup.find_all(tag):
            element.decompose()

    return str(soup)


def extract_tags(html_content, tags: list[str]):
    soup = BeautifulSoup(html_content, 'html.parser')
    text_parts = []

    for tag in tags:
        elements = soup.find_all(tag)
        for element in elements:
            # If the tag is a link (a tag), append its href as well
            if tag == "a":
                href = element.get('href')
                if href:
                    text_parts.append(f"{element.get_text()} ({href})")
                else:
                    text_parts.append(element.get_text())
            else:
                text_parts.append(element.get_text())

    return ' '.join(text_parts)


def scrape_by_url_raw(url: str):
    """
    Scrape the main content text from a given Wikipedia URL.
    """

    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract all the text content. This approach is generalized and
    # might not always yield perfect results for all websites.
    content_text = soup.get_text()

    html_content = response.text

    return html_content


def save_to_txt(content, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)


def remove_unessesary_lines(content):
    # Split content into lines
    lines = content.split("\n")

    # Strip whitespace for each line
    stripped_lines = [line.strip() for line in lines]

    # Filter out empty lines
    non_empty_lines = [line for line in stripped_lines if line]

    # Remove duplicated lines (while preserving order)
    seen = set()
    deduped_lines = [line for line in non_empty_lines if not (
        line in seen or seen.add(line))]

    # Join the cleaned lines without any separators (remove newlines)
    cleaned_content = "".join(deduped_lines)

    return cleaned_content

# This doesn't work well for JavaScript-heavy websites


def scrape(url: str, tags):
    results = remove_unwanted_tags(scrape_by_url_raw(url))

    results_formatted = remove_unessesary_lines(
        extract_tags(remove_unwanted_tags(results), tags=tags))

    # save_to_txt(results_formatted, "scraped_content.txt")

    return results_formatted


async def ascrape_playwright(url, tags: list[str] = ["h1", "h2", "h3", "span"]) -> str:
    print("Started scraping...")
    results = ""
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        try:
            page = await browser.new_page()
            await page.goto(url)

            page_source = await page.content()

            results = remove_unessesary_lines(extract_tags(remove_unwanted_tags(
                page_source), tags))
            print("Content scraped")
        except Exception as e:
            results = f"Error: {e}"
        await browser.close()
    return results


# TESTING
if __name__ == "__main__":
    url = "https://www.patagonia.ca/shop/new-arrivals"

    async def scrape_playwright():
        results = await ascrape_playwright(url)
        print(results)

    pprint.pprint(asyncio.run(scrape_playwright()))
