ecommerce_schema = {
    "properties": {
        "item_name": {"type": "string"},
        "price": {"type": "number"},
        "item_extra_info": {"type": "string"}
    },
    "required": ["item_name", "price", "item_extra_info"],
}

news_schema = {
    "properties": {
        "news_article_title": {"type": "string"},
        "news_article_summary": {"type": "string"},
        "news_article_topic": {"type": "string"}
    },
    "required": ["news_article_title", "news_article_summary", "news_article_topic"],
}
