import scrapy
from scrapy.http import HtmlResponse
from jobparser.items import JobparserItem


class HhruSpider(scrapy.Spider):
    name = 'hhru'
    allowed_domains = ['hh.ru']
    start_urls = ['https://hh.ru/search/vacancy?area=1&fromSearchLine=true&st=searchVacancy&text=Повар&from=suggest_post']

    def parse(self, response:HtmlResponse):
        links = response.xpath("//a[@class='bloko-link HH-LinkModifier']/@href").extract()
        # next_page = response.xpath("//a[contains(@class,'HH-Pager-Controls-Next')]/@href").extract_first()
        for link in links:
            yield response.follow(link, callback=self.vacancy_parse)
        # if next_page:
        #     yield response.follow(next_page, callback=self.parse)


    def vacancy_parse(self,response:HtmlResponse):
        name = response.xpath("//h1/text()").extract_first()
        # salary = response.xpath("//p/span[@data-qa='bloko-header-2']/text()").extract()
        # salary = response.xpath("//p/span[@data-qa='bloko-header-2']/text()").extract()
        min_salary = response.xpath("//p/span[@data-qa='bloko-header-2']/text()").extract()
        try:
            max_salary = [min_salary[3] if 'до ' in min_salary[2] else None]
        except:
            if 'до ' in min_salary[0]:
                max_salary = min_salary[1]
            else:
                max_salary = None
        min_salary = [min_salary[1] if 'от ' in min_salary else None]
        # if len(salary) == 5:
        #     min_salary = salary[1].replace('\xa0', '')
        #     max_salary = salary[3].replace('\xa0', '')
        link = response._url

        print()
        yield JobparserItem(name=name, min_salary=min_salary, max_salary=max_salary, link=link)
