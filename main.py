import asyncio
import pprint

from ai_extractor import extract
from schemas import SchemaNewsWebsites, ecommerce_schema
from scrape import ascrape_playwright

# TESTING
if __name__ == "__main__":
    token_limit = 4000

    cnn_url = "https://www.cnn.com"
    amazon_url = "https://www.amazon.ca/s?k=computers&crid=1LUXGQOD2ULFD&sprefix=%2Caps%2C94&ref=nb_sb_ss_recent_1_0_recent"
    wsj_url = "https://www.wsj.com"

    async def scrape_with_playwright(url: str, **kwargs):
        html_content = await ascrape_playwright(url)

        print("Extracting content with LLM")

        html_content_fits_context_window_llm = html_content[:token_limit]

        extracted_content = extract(**kwargs,
                                    content=html_content_fits_context_window_llm)

        pprint.pprint(extracted_content)

    asyncio.run(scrape_with_playwright(
        url=cnn_url,
        schema_pydantic=SchemaNewsWebsites
    ))
