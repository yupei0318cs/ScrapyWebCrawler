import scrapy

class QQNewsSpider(scrapy.Spider):
    name = 'qqnews'
    start_urls = ['http://society.qq.com/']

    def parse(self, response):

        for url in response.xpath('//*[@id="news"]/div/div/div/em/a/@href'):
            full_url = response.urljoin(url.extract())
            yield scrapy.Request(full_url, callback=self.parse_news)

    def parse_news(self, response):
        title = response.xpath('//*[@id="Main-P-QQ"]/div[1]/h1/text()').extract_first()
        print (title)

