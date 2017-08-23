# -*- coding: utf-8 -*-
import sys
from urlparse import urlparse
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.http import Request
from scrapy.exceptions import CloseSpider
from inventus_spider.items import InventusSpiderItem

class InventusSpider(CrawlSpider):
    name = 'inventus'
    allowed_domains = []
    start_urls = []

    subdomains = []
    subdomain_limit = 0

    rules = (
        Rule(LinkExtractor(), callback='parse_item', follow=True),
    )

    def __init__(self, domain=None, subdomain_limit=10000, *args, **kwargs):
        super(InventusSpider, self).__init__(*args, **kwargs)

        if domain is None:
            print "Error: You must provide a domain."
            return

        self.domain = domain
        self.base_url = 'http://%s' % self.domain
        self.allowed_domains.append(self.domain)
        self.start_urls.append(self.base_url)
        self.subdomain_limit = subdomain_limit

    def parse_item(self, response):
        item = InventusSpiderItem()
        for url in Selector(text=response.body).xpath('//a/@href').extract():
            if not url.startswith('http://') or url.startswith('https://'):
                url = self.base_url + url
            try:
                parsed_uri = urlparse(url)
            except ValueError:
                # If the URL is invalid we can ignore it.
                continue
            if parsed_uri.netloc.endswith('.' + self.domain) and 'mailto:' not in url:
                if not parsed_uri.netloc in self.subdomains:
                    self.subdomains.append(parsed_uri.netloc)
                    item['subdomain'] = parsed_uri.netloc
                    yield item

                    if len(self.subdomains) > int(self.subdomain_limit):
                        break

                yield Request(url, callback=self.parse)

        if len(self.subdomains) >= int(self.subdomain_limit):
            raise CloseSpider('subdomain limit reached')
