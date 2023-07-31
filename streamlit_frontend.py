from ai_extractor import extractor_chain
from scrape import scrape

# TESTING
if __name__ == "__main__":
    html_content = scrape(url="https://www.uploadvr.com")

    print("Extracting content with LLM")
    print(extractor_chain.run(html_content[:3500]))
