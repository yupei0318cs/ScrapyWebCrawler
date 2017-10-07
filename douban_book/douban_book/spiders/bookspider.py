import scrapy
from douban_book.items import DoubanBookItem

class bookSpider(scrapy.Spider):
    '''docstring for BookSpider'''
    name = 'douban_book'
    allowed_domain = ['douban.com']
    #start_urls = ['https://book.douban.com/250']
    start_urls = ['https://movie.douban.com/']

    def parse(self, response):
        yield scrapy.Request(response.url, callback=self.parse_page)
        for page in response.xpath('//div[@class="paginator"]/a'):
            link = page.xpath('@href').extract_first()
            yield scrapy.Request(link, callback=self.parse_page)



    def parse_page(self, response):
        for item in response.xpath('//tr[@class="item"'):
            book = DoubanBookItem
            book.name = item.xpath('td[2]/div[1]/a/@title').extract_first
            book.ratings = item.xpath('td[2]/div[2]/span[@class="rating_nums"]/text()').extract_first
            book_info = item.xpath('/td[2]/p[@class="p1"].text()').extract_first()

            book_info_contents = book_info.strip().split(" / ")
            book.price = book_info_contents[-1]
            book.edition_year = book_info_contents[-2]
            book.publisher = book_info_contents[-3]
            book.author = book_info_contents[-4]





