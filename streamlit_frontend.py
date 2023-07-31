import pprint

from ai_extractor import extractor_chain
from scrape import scrape

# TESTING
if __name__ == "__main__":
    html_content = scrape(
        url="https://www.thehockeyshop.com")

    print("Extracting content with LLM")

    html_content_fits_context_window_llm = html_content[:4000]

    extracted_content = extractor_chain.run(
        html_content_fits_context_window_llm)

    pprint.pprint(extracted_content)

    with open("results.txt", 'w', encoding='utf-8') as file:
        file.write("[{}]".format(", ".join(str(item)
                   for item in extracted_content)))
