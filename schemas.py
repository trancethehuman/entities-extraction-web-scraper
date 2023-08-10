from pydantic import BaseModel

ecommerce_schema = {
    "properties": {
        "item_title": {"type": "string"},
        "item_price": {"type": "number"},
        "item_extra_info": {"type": "string"}
    },
    "required": ["item_name", "price", "item_extra_info"],
}


class SchemaNewsWebsites(BaseModel):
    news_headline: str
    news_short_summary: str
