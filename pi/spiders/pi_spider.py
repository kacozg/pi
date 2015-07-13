import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor

from pi.items import PiItem

class PiSpider(CrawlSpider):
    name = 'pi'
    start_urls = ['http://www.portalinmobiliario.com/venta/departamento/vina-del-mar-valparaiso/5252-edificio-vive-viana-nva?tp=2&op=1&iug=72&ca=3&ts=1&mn=2&or=&sf=0&sp=0&at=0&i=0']

    rules = (
        Rule(LinkExtractor(restrict_xpaths=('//*[@id="wrapper"]/a[2]')), callback='parse_item', follow=True),
    )

    def parse_item(self, response):

        item = PiItem()

        if response.css('body::attr(class)').extract() == [u'page-project']:
            item['url'] = response.url
            item['code'] = response.xpath('//*[@id="wrapper"]/div/section[2]/div/div/div[2]/div[2]/span/text()').extract()
            item['address'] = response.xpath('//*[@id="project-location"]/div/div/div[1]/div/div[1]/p/span[1]/text()').extract()
            item['beds'] = response.xpath('//*[@id="project-features"]/div/div/div[2]/span[2]/em/text()').extract()
            item['baths'] = response.xpath('//*[@id="project-features"]/div/div/div[3]/span[2]/em/text()').extract()
            item['area_total'] = response.xpath('//*[@id="project-features"]/div/div/div[4]/span[2]/text()').extract()
            item['uf'] = response.xpath('//*[@id="wrapper"]/div/section[2]/div/div/div[2]/div[4]/div[1]/div/span[1]/text()').extract()

        else:
            item['url'] = response.url
            item['code'] = response.xpath('//*[@id="wrapper"]/section/div/div/div[1]/article/div/div[2]/div[1]/div[1]/div[2]/p[1]/strong/text()').extract()
            item['address'] =  response.xpath('//*[@id="wrapper"]/section/div/div/div[1]/article/div/div[2]/div[2]/div[2]/div[1]/p/span[1]/text()').extract()
            item['beds'] = response.xpath('//*[@id="wrapper"]/section/div/div/div[1]/article/div/div[2]/div[2]/div[2]/div[2]/p/text()[1]').extract()
            item['baths'] = response.xpath('//*[@id="wrapper"]/section/div/div/div[1]/article/div/div[2]/div[2]/div[2]/div[2]/p/text()[2]').extract()
            item['area_total'] = response.xpath('//*[@id="wrapper"]/section/div/div/div[1]/article/div/div[2]/div[2]/div[2]/div[3]/p/text()[2]').extract()
            item['area_util'] = response.xpath('//*[@id="wrapper"]/section/div/div/div[1]/article/div/div[2]/div[2]/div[2]/div[3]/p/text()[1]').extract()
            item['clp'] = response.xpath('//*[@id="divImagenes"]/div[2]/div/p[1]/text()').extract()
            item['uf'] = response.xpath('//*[@id="divImagenes"]/div[2]/div/p[2]/text()').extract()
            item['date'] = response.xpath('//*[@id="wrapper"]/section/div/div/div[1]/article/div/div[2]/div[1]/div[1]/div[2]/p[2]/strong/text()').extract()
            item['latitude'] = response.xpath('//*[@id="wrapper"]/section/div/div/div[1]/article/div/div[2]/div[2]/div[1]/div[1]/meta[1]/@content').extract()
            item['longitude'] = response.xpath('//*[@id="wrapper"]/section/div/div/div[1]/article/div/div[2]/div[2]/div[1]/div[1]/meta[2]/content').extract()

        return item
