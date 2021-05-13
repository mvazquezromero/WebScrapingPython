

# Extraemos los datos de Mercado Libre para Celulares y Smartphones.
# Queremos saber el Nombre y la Camara Trasera Principal
#

import time
from scrapy import item
from scrapy.item import Field, Item 
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose


#Primero definimos el Item
class MercadoItem(Item):
    telefono = Field() #nombre del telefono
    camaraPrincipal = Field() #Mpx de la camara principal 


#Definimos la Spider // Esto facilita para la crowling vertical y horizontal
class MercadoCrowler(CrawlSpider): 
    
    name = "MELICrowler"
    custom_settings = {
        'USER_AGENT':"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:35.0) Gecko/20100101 Firefox/35.0",
        'CLOSESPIDER_PAGECOUNT':20
        }

    download_delay = 1

    start_urls= ['https://celulares.mercadolibre.com.ar'] #Url Semilla donde arranca el programa
    allowed_domins=['celulares.mercadolibre.com.ar/'] #Lista de dominios a los cuales va spider. //Sirve para que no vaya a publicidades.

    #Creamos las Reglas del crowling, estas reglas le dicen al programa como pasar a la siguiente pagina 
    rules = (
        
        #Paginacion
        Rule(
            LinkExtractor(
                allow=r'/_Desde_'
                ),follow=True
        ), #Detalle de los Productos
        
        Rule(
            LinkExtractor(
                allow=r'/MLA'
                ), follow=True, callback= 'parse_item'
        )
    )
    
    def parse_item(self, response):
        item = ItemLoader(MercadoItem(),response)
        item.add_xpath('camaraPrincipal','//h1/text()')
        item.add_xpath('telefono','//span[@class="ui-pdp-color--BLACK ui-pdp-size--XSMALL ui-pdp-family--SEMIBOLD"]')

        yield item.load_item()
