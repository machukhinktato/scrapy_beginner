import scrapy
from scrapy.http import HtmlResponse
from jobparser.items import JobparserItem
from .variables import *

class SjruSpider(scrapy.Spider):
    name = 'sjru'
    allowed_domains = ['superjob.ru']
    start_urls = ['https://www.superjob.ru/vacancy/search/?keywords=pyrhon&geo%5Bt%5D%5B0%5D=4']

    def parse(self, response):
        pass
