from pathlib import Path
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class QuotesSpider(CrawlSpider):
    name = "crypto"
    start_urls = [
        "https://www.coindesk.com/",
        'https://cointelegraph.com/',
        'https://cryptoslate.com/',
        'https://decrypt.co/',
        'https://www.theblock.co/',
        'https://bitcoinmagazine.com/',
        'https://www.newsbtc.com/',
    ]

    rules = (
        Rule(LinkExtractor(), callback='parse'),
    )

    def parse(self, response):
        yield {
            'url': response.url
        }