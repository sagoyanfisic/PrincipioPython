import urllib, urlparse
from bs4 import BeautifulSoup
#from pdfparser import getTables
#from StringIO import StringIO
from os.path import basename
import shutil

    def download_data():
	    base_url = "http://www.munlima.gob.pe/"
	    data_url = "gobierno-abierto-municipal/transparencia/mml/informacion-de-contrataciones/"
	#Parametros extra

	#Dictionario de elementos :p  
	#items = {
	#	"gasto_publicidad":"gastos-de-publicidad/gastos-de-publicidad",
	#
	#}
	    reporte_url = "gastos-de-publicidad/gastos-de-publicidad"
	#Name
	    name = "gasto_publicidad"
	#
	    download_url = base_url + data_url + reporte_url

	    html = urllib.urlopen(download_url).read() 
	    soup = BeautifulSoup(html)


	    tabs = soup.find("div", {"class", "nn_tabs_content"}).findAll("div", {"class": "nn_tabs_item"})
	#
	    output = {}
	#Getting variables
	    for tab in tabs:
    	
    		    year = tab.find("h2", {"class", "nn_tabs_title"}).contents
	    	    trimestres = tab.findAll("li")
    		    year = str(year)
    		    output[year] = []
    		    links = []
    		    for trimestre in trimestres:
        		    links.append(base_url + trimestre.find("a")['href'])
    		#print links
    		#print year
    		#now the magic
    		    for link in links:
        		    item = download_parse_pdf(link)
			#pass
			    params = urlparse.urlparse(link)
			    print basename(params.path)
			    print item[0]
			    shutil.copy2( item[0],"/home/sagoyanfisic/"+basename(params.path))
	#	print output
    def download_parse_pdf(url):
    #contents = urllib.urlopen(url).read()
        return urllib.urlretrieve(url)

download_data()
