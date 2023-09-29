import scrapy
from scrapy.crawler import CrawlerProcess

"""class MyprojectSpider(scrapy.Spider):
   name = "project"
   allowed_domains = ["dmoz.org"]
   
   start_urls = [
      "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
      "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
   ]
   def parse(self, response):
      for sel in response.xpath('//ul/li'):
         title = sel.xpath('a/text()').extract()
         link = sel.xpath('a/@href').extract()
         desc = sel.xpath('text()').extract()
         print (title, link, desc)"""

class QuoteSpider(scrapy.Spider):
    name = 'quote-spdier'
    start_urls = ['https://quotes.toscrape.com']
    labels= []
    
    def parse(self, response):
        QUOTE_SELECTOR = '.quote'
        TEXT_SELECTOR = '.text::text'
        AUTHOR_SELECTOR = '.author::text'
        
        self.ListarLabels(response.css)

        print(self.labels)
        
        with open('labels.txt','w') as f:
           
           for item in self.labels:
               
              f.write("%s\n" % item)

        """for quote in response.css(QUOTE_SELECTOR):
            yield {
                'text': quote.css(TEXT_SELECTOR).get(),
                'author': quote.css(AUTHOR_SELECTOR).get(),
                
            }"""
                       
    def ListarLabels(self, response):
               
        TAGS= '.tags'
        TAG_SELECTOR= '.tag::text'
        
        for tag in response(TAGS):
              
           self.labels.append(tag.css(TAG_SELECTOR).getall())
            

process = CrawlerProcess(
    settings={
        "FEEDS": {
            "items.json": {"format": "json", "overwrite":True},
        },
    }
)

process.crawl(QuoteSpider)
process.start()

print("")
print("")
print("")
print("")
print("LO LOGREEEEEEE CTMMMMMMMMM")

