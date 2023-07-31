from typing import List, Optional

from pydantic import BaseModel, Field

ecommerce_schema = {
    "properties": {
        "item_title": {"type": "string"},
        "item_price": {"type": "number"},
        "item_extra_info": {"type": "string"}
    },
    "required": ["item_name", "price", "item_extra_info"],
}


class SchemaNewsWebsites(BaseModel):
    news_article_title: str
    news_article_summary: str
    news_article_extra_info: str
