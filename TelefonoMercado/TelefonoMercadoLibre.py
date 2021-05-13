

# Extraemos los datos de Mercado Libre para Celulares y Smartphones.
# Queremos saber el Nombre y la Camara Trasera Principal
#

import time
from typing import FrozenSet
from scrapy import item
from scrapy.item import Field, Item 
from scrapy.spiders import CrawlSpider, Rule
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
    start_urls= ['https://celulares.mercadolibre.com.ar'] #Url Semilla donde arranca el programa
    allowed_domins=['celulares.mercadolibre.com.ar/'] #Lista de dominios a los cuales va spider. //Sirve para que no vaya a publicidades.

    #Creamos las Reglas del crowling, estas reglas le dicen al programa como pasar a la siguiente pagina 
    rules = (
        Rule(LinkExtractor(allow=r'_Desde_')), #La spider solo puede entrar a URL que contengan MLA (nro de serie de mercado libre)
        Rule(LinkExtractor(allow=r'MLA'), callback= 'parse_item')
    )

    def parse_item(self, response):
        item = ItemLoader(MercadoItem(),response)
        item.add_xpath('camaraPrincipal','//*[@id="highlighted-specs"]/div[3]/div/div[2]/div/div/div[2]/p/span[2]/text()')
        item.add_xpath('telefono','//*[@id="root-app"]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/h1/text()')

        yield item.load_item()
