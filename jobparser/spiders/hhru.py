import scrapy
from scrapy.http import HtmlResponse
from jobparser.items import JobparserItem
from .variables import *

class HhruSpider(scrapy.Spider):
    name = 'hhru'
    allowed_domains = ['hh.ru']
    start_urls = [
        'https://hh.ru/search/vacancy?area=1&fromSearchLine=true&st=searchVacancy&text=Повар&from=suggest_post']

    def parse(self, response: HtmlResponse):
        links = response.xpath("//a[@class='bloko-link HH-LinkModifier']/@href").extract()
        # next_page = response.xpath("//a[contains(@class,'HH-Pager-Controls-Next')]/@href").extract_first()
        for link in links:
            yield response.follow(link, callback=self.vacancy_parse)
        # if next_page:
        #     yield response.follow(next_page, callback=self.parse)

    def vacancy_parse(self, response: HtmlResponse):
        name = response.xpath(hh_name).extract_first()
        min_salary = response.xpath(hh_salary).extract()
        max_salary = None
        try:
            if 'до ' in min_salary[2]:
                max_salary = min_salary[3]
            elif 'до ' in min_salary[0]:
                max_salary = min_salary[1]
        except:
            max_salary = None
        min_salary = [min_salary[1] if 'от ' in min_salary else None][0]
        link = response.url

        print()
        yield JobparserItem(name=name, min_salary=min_salary, max_salary=max_salary, link=link)
