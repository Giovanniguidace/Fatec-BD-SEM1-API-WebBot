# <B>Projeto Web BOT:</b>

<b>Objetivo do API:</b>
		<p>O objetivo do API do primeiro semestre, consiste em criar um WEBBOT para automatizar qualquer tipo de operação que será escolhida de forma livre entre as equipes. </p>



<b>Objetivo do Projeto:</b>

![logo.jpg](https://gitlab.com/cesaraugusto98/webbot/-/raw/master/class/logo.jpg)

Criar um WebBOT capaz de realizar a leitura de CNPJ's de todas as empresas de São José dos Campos e realizar a leitura de qual o tipo de ramo cada empresa. Será possível também, validar qual o capital a empresa possui e se ela está inativa ou ativa.

Com este valores coletados e os pontos inseridos no mapa, será possível visualizar em regiões de São José dos Campos quais delas possuem uma maior quantia de empresa de determinado ramo e capital. 

É possível selecionar no mapa qual ramo e capital deverá ser filtrado. Esta opção é disponibilizada aos usuários para que possam saber se determinada região compensa um possível investimento em determinado ramo.

Caso de Uso do Projeto:

![IMG-20190827-WA0037.jpg](https://gitlab.com/cesaraugusto98/webbot/-/raw/Mapas_geolocaliza%C3%A7ao/Imagens/IMG-20190827-WA0037.jpg)


<b>Tecnologias Adotadas na Solução:</b>

* Slack - Motivo: Utilizado como meio principal de contato entre a equipe;
* Visual Studio Code - Motivo: De acordo com votação em equipe, foi decidido a utilização desta ferramenta para desenvolvimento do código;
* MongoDB - Motivo: De acordo com votação em equipe, foi utilizado este banco não relacional para armazenar dados de CNPJ, Ramo da empresa, Latitude e Longitude, Capital;
* Django/Python: Motivo: De acordo com votação em equipe, foi decidido pelo Django Framework devido a sua linguagem ser em python e pela possibilidade de utilizar bibliotecas de geolocalização, organização de dados, entre outros...

	<b>Bibliotecas Python Utilizadas:</b>
	*   Selenium - Utilizado para coletar informações de empresa e geolocalização em sites;
	*   OS - Biblioteca Python;
	*   Math - Biblioteca Python;
	*   Pymongo - Utilizado para conectar no servidor do BD NoSQL Mongo;
	*   Folium - Utilizado para apontar Latitude e Longitude no mapa geográfico;
	*   Pandas - Utilizado para organizar dados de empresa e posteriormente enviar para a biblioteca Folium;

<b>Contribuições individuais/pessoais</b>

* Levantamento de tecnologias a serem utilizadas;
* Auxilio no levantamento dos objetivos do projeto;
* Coletar Latitude e Longitude de cada empresa e apontar em um mapa os pontos utilizando a biblioteca Folium e Pandas;
* Apresentação do projeto;

Utilização da biblioteca Folium - Na prática:

Primeiramente, foi realizada a conexão com a base de dados NoSQL MongoDB, no qual as informações de Latitude e Longitude estavam armazenadas. Com isso, foi possível utilizar a Lib do Folium para criar um mapa de calor e um mapa de pontos em uma determinada região, que no projeto foi escolhida São José dos Campos.

Mapa de calor:
```python
import pymongo
import folium

from folium import plugins
from pymongo import MongoClient

#REALIZA A CONEXÃO COM O BANCO NO MONGO DB
db = MongoClient('mongodb+srv://admin:admin@cluster0-vuh1j.azure.mongodb.net/test?retryWrites=true&w=majority')

db = db.get_database('BD_EMPRESAS')


collection = db.empresas
latitude = []
longitude = []
qtd_range = []
coordenadas = []

#GET DE TODAS AS LATITUDES NA COLLECTION EMPRESAS
latitude = db.get_collection('empresas').distinct("latitude")

qtd_range = len(latitude)

#GET DE TODAS AS LONGITUDES NA COLLECTION EMPRESAS
longitude = db.get_collection('empresas').distinct("longitude")

#DELIMITA A REGIÃO DE INTERESSE NA BIBLIOTECA FOLIUM
mapa = folium.Map(location=[-23.4795233,-46.2698754],zoom_start=9)

#É ADICIONADO NO MAPA OS PONTOS COM AS LOCALIZAÇÕES DE LATITUDE E LONGITUDE
for i in range(qtd_range):
 coordenadas.append([latitude[i],longitude[i]])
 mapa.add_child(plugins.HeatMap(coordenadas))
 
#OS PONTOS SÃO ENVIADOS PARA O TEMPLATE MAPA_CALOR.HTML E SÃO TRANSFORMADOS COMO MAPA DE CALOR
mapa.save("mapa_calor.html")

```

Mapa de pontos:
```python
import pymongo
import folium

from pymongo import MongoClient

#REALIZA A CONEXÃO COM O BANCO NO MONGO DB
db = MongoClient('mongodb+srv://admin:admin@cluster0-vuh1j.azure.mongodb.net/test?retryWrites=true&w=majority')

db = db.get_database('BD_EMPRESAS')

collection = db.empresas
cnpj = []
latitude = []
longitude = []
qtd_range = []
endereco = []

#REALIZA A COLETA DE DADOS DA EMPRESA NA COLLECTION EMPRESAS
cnpj = db.get_collection('empresas').distinct("cnpj")
latitude = db.get_collection('empresas').distinct("latitude")
qtd_range = len(latitude)
longitude = db.get_collection('empresas').distinct("longitude")
endereco = db.get_collection('empresas').distinct("endereco")

#DELIMITA A REGIÃO DE INTERESSE NA BIBLIOTECA FOLIUM
mapa = folium.Map(location=[-23.4795233,-46.2698754],zoom_start=9)

for i in range(qtd_range):
 folium.Marker([latitude[i], longitude[i]], popup='CNPJ: '+cnpj[i]+'\n Endereco: '+endereco[i]).add_to(mapa)

#É ADICIONADO NO MAPA OS PONTOS COM AS LOCALIZAÇÕES DE LATITUDE E LONGITUDE
mapa.save("mapa_pontos.html")

```


<b>Aprendizados Efetivos</b>

* Trabalho em equipe utilizando a metodologia ágil SCRUM:
	* Através de Daily's, Sprints, Plannings, Reviews, foi possível entender como funciona de fato a metodologia ágil e qual a proposta de sua implantação em projetos de desenvolvimento.

* Aprofundamento na linguagem Python e as bibliotecas Folium e Pandas:
	* A linguagem Python foi trazida desde o início do curso e foi desenvolvida durante os semestres, com isso, foi possível compreender suas características e qual é a sua finalidade de utilização. As bibliotecas Folium e Pandas foram importadas e utilizadas no projeto e com isso, foi possível compreender que além destas, outras várias Lib's se encontram disponíveis para serem importadas e utilizadas;
	
* Organização de projeto e documentação:
	* A etapa de documentação foi trazida como requisito do projeto, e os itens para compor a documentação são:
		* Caso de Uso;
		* Modelo Entidade Relacionamento de Banco de Dados;
		* Métricas de BurnDown e conclusão de Sprints;
		* Matriz de Habilidade de cada integrante;
		
* Inicialização no framework Django:
	* O Framework Django utiliza da linguagem Python para que possamos, de maneira rápida e ágil, criar aplicações Web. Neste projeto foi aprendido a criar o projeto Django e adicionar Apps para que fossem assim criadas as funcionalidades do projeto. Com a conclusão do projeto, foi possível subir o server do Django e publicar o projeto na Web;
	
* Funcionamento de web scraping;
	* Para a coleta de dados de CNPJ e outros dados de empresa e também Latitude e Longitude de sua localização, foi utilizado o Web Scraping, que é um método de coleta de dados através dos templates em html dos sites visitados. 

Coleta de dados utilizando Web Scraping
```python
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep

class Driver:

#MAPEAMENTO DO __INIT__ PARA A LOCALIZAÇÃO DE ARQUIVOS
 def __init__(self, cep=False, cnpj=False):
		 directory = 'E:\\FATEC\\PI\\Files'
		 chrome_options = webdriver.ChromeOptions()
		 preferences = {"download.default_directory": directory}
		 chrome_options.add_experimental_option("prefs", preferences)
		 self.driver = webdriver.Chrome(chrome_options=chrome_options, executable_path='C:\\webbot\\chromedriver')
		 self.wait = WebDriverWait(self.driver, 5)
		 self.cep = cep
		 self.cnpj = cnpj
		 self.openSite()
 # self.driver.close()
 
 #FUNÇÃO QUE FARÁ O ACESSO AO SITE DE MAPA CEP E COLETARÁ DADOS DE LATITUDE E LONGITUDE DE ACORDO COM O CEP COLETADO NOS DADOS DA EMPRESA 
 def openSite(self):
		 self.driver.maximize_window()
		 self.driver.get("https://www.mapacep.com.br/index.php")
		 self.wait.until(EC.presence_of_element_located((By.ID, 'keywords')))
		 self.driver.find_element_by_id('keywords').send_keys(self.cep)
		 self.driver.find_element_by_xpath('/html/body/header/div[1]/div/div[2]/div/form/span/button').click()
		 sleep(10)
		 print(self.driver.find_element_by_xpath('/html/body/main/div[3]/div/div[1]/p').text)
		 text = self.driver.find_element_by_xpath('/html/body/main/div[3]/div/div[1]/p').text.split('\n')
		 # print(text)
		 # exit()
		 endereco = text[0]
		 latitude = text[3].split(' ')[1]
		 longitude = text[4].split(' ')[1]
		 print([latitude, longitude, endereco])
		 if self.cnpj:
				 try:
				 self.wait.until(EC.presence_of_element_located((By.ID, 'keywords')))
				 self.driver.find_element_by_id('keywords').clear()
				 self.driver.find_element_by_id('keywords').send_keys(self.cnpj[0:14])
				 self.driver.find_element_by_xpath('/html/body/header/div[1]/div/div[2]/div/form/span/button').click()
				 sleep(10)
				 text_cnpj = self.driver.find_element_by_xpath('/html/body/main/div[5]/div/div[1]/p[1]').text
				 text_cnpj = text_cnpj.split('\n')
				 print(text_cnpj)
				 codigo_atividade = text_cnpj[6].split(' ')[7]
				 nome_empresarial = text_cnpj[4].split(': ')[1]
				 descricao = text_cnpj[6].split(' ')[9:]
				 # self.driver.close()
				 return [latitude, longitude, endereco, codigo_atividade, nome_empresarial]
		 except:
				 # self.driver.close()
				 return [latitude, longitude]
		 # self.driver.quit()
		 # print(endereco, latitude, longitude)

#FUNÇÃO QUE REALIZA O DOWNLOAD DO ARQUIVO CONTENDO DADOS DE EMPRESAS
def getArchives(self):
		 self.driver.get(
		 'http://receita.economia.gov.br/orientacao/tributaria/cadastros/cadastro-nacional-de-pessoas-juridicas-cnpj/dados-publicos-cnpj')
		 links = self.driver.find_elements_by_css_selector('a.external-link')
		 for link in links:
				 link.click()
				 sleep(1)
				 self.waitDownload()

#FUNÇÃO QUE AUXILIA NO DOWNLOAD DE ARQUIVOS CONTENDO DADOS DE EMPRESAS 	 
def waitDownload(self):
		 if not self.driver.current_url.startswith("chrome://downloads"):
				 self.driver.get("chrome://downloads/")
				 # elemento = self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="leftSpacer"]/h1')))
				 retorno = self.driver.execute_script("""
				 var items = downloads.Manager.get().items_;
				 if (items.every(e => e.state === "COMPLETE"))
				 return items.map(e => e.fileUrl || e.file_url);
				 else
				 return false
				 """)
				 # print(retorno)
				 count = 0
		 while retorno == False and count < 15:
				 sleep(1)
				 retorno = self.driver.execute_script("""
				 var items = downloads.Manager.get().items_;
				 if (items.every(e => e.state === "COMPLETE"))
				 return items.map(e => e.fileUrl || e.file_url);
				 else
				 return false
				 """)
				 count += 1
				 # print(retorno)
				 return
```

#
