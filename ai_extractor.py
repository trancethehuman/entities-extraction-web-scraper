import os

from dotenv import load_dotenv
from langchain.chains import (create_extraction_chain,
                              create_extraction_chain_pydantic)
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

load_dotenv()

openai_api_key = os.getenv('OPENAI_API_KEY')

llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo-0613",
                 openai_api_key=openai_api_key)

schema = {
    "properties": {
        "item_name": {"type": "string"},
        "url": {"type": "string"},
        "price": {"type": "string"},
    },
    "required": ["item_name", "url", "price"],
}

extractor_chain = create_extraction_chain(schema, llm)
