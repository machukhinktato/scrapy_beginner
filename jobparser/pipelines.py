# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient



class JobparserPipeline:
    def __init__(self):
        client = MongoClient('localhost',27017)
        self.mongo_base = client.vacansy1911
        print()


    def process_item(self, item, spider):
        collection = self.mongo_base[spider.name]
        try:
            item['_id'] = collection.count_documents({}) + 1
        except:
            item['_id'] = 1
        collection.insert_one(item)
        # if spider.name == 'hhru':
        #     self.process_salary_hh(item['salary'])


        print()
        return item

    # def process_salary(self,salary):
    #
    #     return salary_min, salary_max, currency