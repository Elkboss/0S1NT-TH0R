import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
import re
import colorama
from colorama import Fore, Back, Style
import json
#------End modules-----------#
colorama.init()
busqueda = input(Fore.GREEN+"Introdueix la teva cerca: "+Style.RESET_ALL)

options = Options()
options.headless = True
driver = webdriver.Chrome(options=options, executable_path=("C:/Users/Elkboss/Desktop/chromedriver.exe"))
driver.get('https://archive.org/search.php?query={0}'.format(str(busqueda)))
#driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(5)
element = driver.find_elements_by_class_name("item-ia.hov")
print(len(element))
data_id=list()
type_element = list()
fecha = list()
k=0
for x in element:
	name = x.get_attribute("data-id")
	data_type = x.get_attribute("data-mediatype")
	fecha_scrape = x.get_attribute("data-year")
	fecha.append(fecha_scrape)
	type_element.append(data_type)
	data_id.append(name)
	#print(Fore.RED+" Titulo: "+str(data_id[k])+" Fecha de publicacion: "+str(fecha[k])+" Tipo de contenido: "+str(type_element[k]))
	k=k+1
correu = list()
j=0
for y in data_id:
	url = 'https://archive.org/download/{0}/{0}_meta.xml'.format(str(y))#print(url)
	response = requests.get(url)
	html = BeautifulSoup(response.text, 'html.parser')
	find = re.findall(r'[\w\.-]+@[\w\.-]+', response.text, re.I)
	correu.append(find)
	print(data_id[j]+" "+str(correu[j]))
	print(" ")
	j=j+1
f = open("archiveorg.json","w")
e=0
for y in range(len(data_id)):
	f.write('\n{'+'"Publicacion"'+':'+'[{'+'"Titulo"'+':'+'"'+str(data_id[e])+'"'+','+'"Fecha Publicacion"'+':'+'"'+str(fecha[e])+'"'+','+'"Correo Electronico"'+':'+'"'+str(correu[e])+'"'+','+'"Usuario"'+':'+'"dsdsad"'+'}]}')
	#print("Títol:"+str(data_id[e])+" Data de Publicació: "+str(fecha[e])+" Correu Electronic: "+str(correu[e]+" "))
	e=e+1
f.close()
