from bs4 import BeautifulSoup
import requests
import time

coin_url = input("INGRESE CRYPTO: ")		#Ingreamos la crypto moneda que quiere consultar
coin_url = coin_url.lower()

r = requests.get(f"https://www.coindesk.com/price/{coin_url}") #link 
soup = BeautifulSoup(r.content, "lxml")

def imprimirPrecio():
    #Precio del dia#
    crypto_price = soup.find('div',class_="price-large").text
    #CRYPTO + TICKER#
    crypto = soup.find('li',class_ ="breadcrumbs-item active").text
    coin = soup.find('span',class_ ="coin-iso").text
    alltime_max = soup.find('div',class_ ="price-small")

    print(f"{crypto}, {coin}: Su precio actual es: {crypto_price} ")  
    print()

imprimirPrecio()

#Version Beta, proximamente: 
#Expresar fecha y hora de la Crypto
##Consultar otras cryptos al finalizar una consulta

#Version 2.0: Hacer una consulta diaria y ingresarla en xslx o csv.
