## Web Scrapping de MercadoLibre
* Python 3.9
* Scrapy 2.5


### Generamos una araña que va a ingresar a cada telefono y devolver NOMBRE DEL SMARTPHONE y Mpx de la CAMARA FROTNAL PRINCIPAL
Para descargar los primero 20 articulos en un .csv ingresar en la carpeta el cmd :
* >scrapy runspider TelefonoMercadoLibre.py -o TelefonoMercadoLibre.csv -t csv --set CLOSESPIDER_ITEMCOUNT=20 

