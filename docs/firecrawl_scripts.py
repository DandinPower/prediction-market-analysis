import os

from dotenv import load_dotenv
from firecrawl import Firecrawl

load_dotenv()

FIRECRAWL_API_KEY = os.getenv("FIRECRAWL_API_KEY")

firecrawl = Firecrawl(api_key=FIRECRAWL_API_KEY)

CRAWL_WEBSITE = "https://docs.polymarket.com/"
CRAWL_LIMIT = 200

result = firecrawl.crawl(
    url=CRAWL_WEBSITE,
    limit=CRAWL_LIMIT,
    scrape_options={
        "formats": ["markdown"],
        "only_main_content": True,
    },
    poll_interval=30,
)

# Can go to https://www.firecrawl.dev/app/logs for downloading markdowns