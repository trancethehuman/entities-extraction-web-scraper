import os

from dotenv import load_dotenv
from langchain.chains import (create_extraction_chain,
                              create_extraction_chain_pydantic)
from langchain.chat_models import ChatOpenAI

load_dotenv()

openai_api_key = os.getenv('OPENAI_API_KEY')

llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo-0613",
                 openai_api_key=openai_api_key)


def extract(schema, content: str):
    return create_extraction_chain(schema, llm).run(content)
