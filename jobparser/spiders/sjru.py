import scrapy
from scrapy.http import HtmlResponse
from jobparser.items import JobparserItem
from .variables import *

class SjruSpider(scrapy.Spider):
    name = 'sjru'
    allowed_domains = ['superjob.ru']
    start_urls = ['https://www.superjob.ru/vacancy/search/?keywords=pyrhon&geo%5Bt%5D%5B0%5D=4']


    def parse(self, response:HtmlResponse):
        url = 'https://www.superjob.ru'
        links = response.xpath("//a[contains(@class, 'icMQ_ _6AfZ9')]/@href").extract()
        for link in links:
            yield response.follow(url + link, callback=self.vacancy_parse)
        print()


    def vacancy_parse(self, response:HtmlResponse):
        name = response.xpath(sj_name)
        salary = response.xpath(sj_salary).extract
        link = response._url
        print()
