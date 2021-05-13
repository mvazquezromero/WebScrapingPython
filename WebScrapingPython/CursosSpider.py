from scrapy.item import Item
from scrapy.item import Field
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.loader import ItemLoader

#Problema: Extraer infromacion de eddx.org - Cursos de Python en Español. 

class Cursos(Item):
    cursos = Field()
    id = Field()
    
class EdxOrg(Spider):
    name = "MiEdxSpider"
    start_urls = ['https://www.edx.org/es/search?language=Español&q=python&tab=course']
    def parse(self, response):
        sel = Selector(response)
        #ingresamos con xpath al div class donde se encuentran los cursos y seleccionamos todas sus celas hijas que sean un div
        cursos = sel.xpath('//div[@class_="static-card-list d-flex m-xl-0 p-0 flex-wrap"]/div') 
        
        #Iterar sobre todos los Cursos.
        for i, elem in enumerate(cursos):
            item = ItemLoader(Cursos(), elem)
            item.add_xpath('cursos','.//div/text()')
            item.add_value('id',1)
            yield item.load_item()