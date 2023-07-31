import pprint

from ai_extractor import extract
from schemas import ecommerce_schema, news_schema
from scrape import scrape

# TESTING
if __name__ == "__main__":
    html_content = scrape(
        url="https://appsumo.com/courses-learning/")

    pprint.pprint(html_content)

    print("Extracting content with LLM")

    html_content_fits_context_window_llm = html_content[:4000]

    extracted_content = extract(schema=ecommerce_schema,
                                content=html_content_fits_context_window_llm)

    pprint.pprint(extracted_content)
