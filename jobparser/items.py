import scrapy


class JobparserItem(scrapy.Item):
    _id = scrapy.Field()
    name = scrapy.Field()
    min_salary = scrapy.Field()
    max_salary = scrapy.Field()
    link = scrapy.Field()
    print()


# class JobparserItem(scrapy.Item):
#     _id = scrapy.Field()
#     name = scrapy.Field()
#     min_salary = scrapy.Field()
#     max_salary = scrapy.Field()
#     link = scrapy.Field()
#     print()