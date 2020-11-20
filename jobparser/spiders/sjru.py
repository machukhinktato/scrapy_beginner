import scrapy
from scrapy.http import HtmlResponse
from jobparser.items import JobparserItem
from .variables import *


class SjruSpider(scrapy.Spider):
    name = 'sjru'
    allowed_domains = ['superjob.ru']
    # start_urls = ['https://www.superjob.ru/vacancy/search/?keywords=python&geo%5Bt%5D%5B0%5D=4']
    # start_urls = ['https://www.superjob.ru/vakansii/testirovshik.html?geo%5Bt%5D%5B0%5D=4']
    start_urls = ['https://www.superjob.ru/vakansii/testirovschik.html?geo%5Bt%5D%5B0%5D=4']

    def parse(self, response: HtmlResponse):
        links = response.xpath("//a[contains(@class, 'icMQ_ _6AfZ9')]/@href")
        next_page = response.xpath("//a[contains(@class, 'f-test-button-dalshe')]/@href").extract_first()
        for link in links:
            yield response.follow(link, callback=self.vacancy_parse)
        if next_page:
            yield response.follow(next_page, callback=self.parse)


    def vacancy_parse(self, response: HtmlResponse):
        min_salary, max_salary = locals()
        name = response.xpath(sj_name).extract_first()
        if 'По договорённости' in response.xpath(sj_salary).extract():
            min_salary = None
            max_salary = None
        else:
            min_salary = response.xpath(sj_salary).extract()
            if '—' in min_salary:
                max_salary = min_salary[4].replace('\xa0', '')
                min_salary = min_salary[0].replace('\xa0', '')
            elif 'до' in min_salary:
                max_salary = min_salary[2].replace('\xa0', '').split('руб.')[0]
                min_salary = None
            else:
                max_salary = None
                min_salary = min_salary[2].replace('\xa0', '').split('руб.')[0]
        link = response.url

        print()
        yield JobparserItem(name=name, min_salary=min_salary, max_salary=max_salary, link=link)
