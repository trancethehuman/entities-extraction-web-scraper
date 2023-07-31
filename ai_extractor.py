import os

from dotenv import load_dotenv
from langchain.chains import (create_extraction_chain,
                              create_extraction_chain_pydantic)
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

openai_api_key = os.getenv('OPENAI_API_KEY')

llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo-0613",
                 openai_api_key=openai_api_key)

schema = {
    "properties": {
        "article_name": {"type": "string"},
        "url": {"type": "string"},
        "author": {"type": "string"}
    },
    "required": ["article_name", "url", "author"],
}

extractor_chain = create_extraction_chain(schema, llm)
