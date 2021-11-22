import requests
from bs4 import BeautifulSoup
import Funciones_Scrapper
import re
import Funciones_Scrapper

page = requests.get("https://www.normacomics.com/guardianes-de-la-noche-11.html")
soup= BeautifulSoup(page.content,'html.parser')


#print(soup.encode("utf-8"))


#result=soup.find("p", { "class" : "availability" }).find("span", recursive=False)
result = soup.select_one('p.availability > span')

stock=result.text
print(stock)
print('Analizando los datos...')


#Establecemos el precio deseado
#precioDeseado = 7
#global HayOferta
#Calcula el precio
#print ("\nEl precio máximo deseado para este producto es de "+ str(precioDeseado)+"€\n")

#global hayOferta
#Calcula el precio
#hayOferta = Funciones_Scrapper.Oferta_Precio_Deseado(precioActual,precioDeseado)

if(stock=="En stock"):
    print("Tenemos Stock! - Avisamos al usuario!")
    #avisar por telegram
    import Aviso_Telegram
    Aviso_Telegram
else:
    print("No hay oferta.")

#2089233941:AAFA_md4pvCXgVCB68wkhiOBLc4POIlcDPA
#735937105




