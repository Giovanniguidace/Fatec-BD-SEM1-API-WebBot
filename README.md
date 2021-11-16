


# <B>Desafio: Web Bot</b>

## :orange_book: <b>Desafio da API:</b>
O desafio do API do primeiro semestre, consiste em criar um WEBBOT para automatizar qualquer tipo de operação que será escolhida de forma livre entre as equipes. 



## <b>:dart: Objetivo da Aplicação Pesquisa Empresas</b>

![logo.jpg](https://gitlab.com/cesaraugusto98/webbot/-/raw/master/class/logo.jpg)

Criar um WebBOT capaz de realizar a leitura de CNPJ's de todas as empresas de São José dos Campos e realizar a leitura de qual o tipo de ramo cada empresa. Será possível também, validar qual o capital a empresa possui e se ela está inativa ou ativa.

Com este valores coletados e os pontos inseridos no mapa, será possível visualizar em regiões de São José dos Campos quais delas possuem uma maior quantia de empresa de determinado ramo e capital. 

É possível selecionar no mapa qual ramo e capital deverá ser filtrado. Esta opção é disponibilizada aos usuários para que possam saber se determinada região compensa um possível investimento em determinado ramo.

Caso de Uso do Projeto:

![IMG-20190827-WA0037.jpg](https://gitlab.com/cesaraugusto98/webbot/-/raw/Mapas_geolocaliza%C3%A7ao/Imagens/IMG-20190827-WA0037.jpg)


## <b>⚙️ Tecnologias Adotadas na Solução:</b>

* Slack - Motivo: Utilizado como meio principal de contato entre a equipe;
* Visual Studio Code - Motivo: De acordo com votação em equipe, foi decidido a utilização desta ferramenta para desenvolvimento do código;
* MongoDB - Motivo: De acordo com votação em equipe, foi utilizado este banco não relacional para armazenar dados de CNPJ, Ramo da empresa, Latitude e Longitude, Capital;
* Flask/Python: Motivo: De acordo com votação em equipe, foi decidido pelo Flask Framework devido a sua linguagem ser em python e pela possibilidade de utilizar bibliotecas de geolocalização, organização de dados, entre outros...

	<b>Bibliotecas Python Utilizadas:</b>
	*   Selenium - Utilizado para coletar informações de empresa e geolocalização em sites;
	*   OS - Biblioteca Python;
	*   Math - Biblioteca Python;
	*   Pymongo - Utilizado para conectar no servidor do BD NoSQL Mongo;
	*   Folium - Utilizado para apontar Latitude e Longitude no mapa geográfico;
	*   Pandas - Utilizado para organizar dados de empresa e posteriormente enviar para a biblioteca Folium;

## <b> :wrench: Contribuições individuais/pessoais</b>

* Levantamento de tecnologias a serem utilizadas;
* Auxilio no levantamento dos objetivos do projeto;
* Coletar Latitude e Longitude no banco de dados e inserir em um mapa de calor e de pontos utilizando a biblioteca Folium e Pandas;
* Apresentação do projeto;

Utilização da biblioteca Folium - Na prática:

Primeiramente, foi realizada a conexão com a base de dados NoSQL MongoDB, no qual as informações de Latitude e Longitude estavam armazenadas. Com isso, foi possível utilizar a Lib do Folium para criar um mapa de calor e um mapa de pontos em uma determinada região, que no projeto foi escolhida São José dos Campos.

Mapa de calor:
```python
1 import pymongo
2 import folium
3 
4 from folium import plugins
5 from pymongo import MongoClient
6  
7 #REALIZA A CONEXÃO COM O BANCO NO MONGO DB
8 db = MongoClient('mongodb+srv://admin:admin@cluster0-vuh1j.azure.mongodb.net/test?retryWrites=true&w=majority')
9  #CONECTA AO BANCO DE DADOS "BD_EMPRESAS"
10 db = db.get_database('BD_EMPRESAS')
11
12
13 collection = db.empresas
14 latitude = []
15 longitude = []
16 qtd_range = []
17 coordenadas = []
18 
19 #GET DE TODAS AS LATITUDES NA COLLECTION EMPRESAS
20 latitude = db.get_collection('empresas').distinct("latitude")
21
22 qtd_range = len(latitude)
23
24 #GET DE TODAS AS LONGITUDES NA COLLECTION EMPRESAS
25 longitude = db.get_collection('empresas').distinct("longitude")
26
27 #DELIMITA A REGIÃO DE INTERESSE NA BIBLIOTECA FOLIUM
28 mapa = folium.Map(location=[-23.4795233,-46.2698754],zoom_start=9)
29
30 #É ADICIONADO NO MAPA OS PONTOS COM AS LOCALIZAÇÕES DE LATITUDE E LONGITUDE
31 for i in range(qtd_range):
32 		coordenadas.append([latitude[i],longitude[i]])
33      mapa.add_child(plugins.HeatMap(coordenadas))
34
35 #OS PONTOS SÃO ENVIADOS PARA O TEMPLATE MAPA_CALOR.HTML E SÃO TRANSFORMADOS COMO MAPA DE CALOR
36 mapa.save("mapa_calor.html")

```
Exemplo de mapa de calor:

![image](https://user-images.githubusercontent.com/62898187/141614915-55a893ba-451e-4d4d-b901-8b94bf7dd9ef.png)


Mapa de pontos:
```python
1 import pymongo
2 import folium
3
4 from pymongo import MongoClient
5 
6 #REALIZA A CONEXÃO COM O BANCO NO MONGO DB
7 db = MongoClient('mongodb+srv://admin:admin@cluster0-vuh1j.azure.mongodb.net/test?retryWrites=true&w=majority')
8 #CONECTA AO BANCO DE DADOS "BD_EMPRESAS"
9 db = db.get_database('BD_EMPRESAS')
10
11 collection = db.empresas
12 cnpj = []
13 latitude = []
14 longitude = []
15 qtd_range = []
16 endereco = []
17
18 #REALIZA A COLETA DE DADOS DA EMPRESA NA COLLECTION EMPRESAS
19 cnpj = db.get_collection('empresas').distinct("cnpj")
20 latitude = db.get_collection('empresas').distinct("latitude")
21 qtd_range = len(latitude)
22 longitude = db.get_collection('empresas').distinct("longitude")
23 endereco = db.get_collection('empresas').distinct("endereco")
24 
25 #DELIMITA A REGIÃO DE INTERESSE NA BIBLIOTECA FOLIUM
26 mapa = folium.Map(location=[-23.4795233,-46.2698754],zoom_start=9)
27 
28 for i in range(qtd_range):
29	   folium.Marker([latitude[i], longitude[i]], popup='CNPJ: '+cnpj[i]+'\n Endereco: '+endereco[i]).add_to(mapa)
30
31 #É ADICIONADO NO MAPA OS PONTOS COM AS LOCALIZAÇÕES DE LATITUDE E LONGITUDE
32 mapa.save("mapa_pontos.html")

```
Exemplo mapa de pontos:

![image](https://user-images.githubusercontent.com/62898187/141614935-6b9282a0-4edb-4803-9440-74d1cf72eae8.png)

## <b>🧠 Aprendizados Efetivos</b>

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
	* O Framework Django utiliza da linguagem Python para que possamos, de maneira rápida e ágil, criar aplicações Web. Mesmo que esta tecnologia não tenha sido utilizada, neste projeto foi aprendido a criar o projeto Django e adicionar Apps para que fossem assim criadas as funcionalidades do projeto. Com a conclusão do projeto, foi possível subir o server do Django e publicar o projeto na Web;
	
* Funcionamento de web scraping;
	* Para a coleta de dados de CNPJ e outros dados de empresa e também Latitude e Longitude de sua localização, foi utilizado o Web Scraping, que é um método de coleta de dados através dos templates em html dos sites visitados. 

Coleta de dados utilizando Web Scraping
```python
1 from selenium import webdriver
2 from selenium.webdriver.support.ui import WebDriverWait
3 from selenium.webdriver.support import expected_conditions as EC
4 from selenium.webdriver.common.by import By
5 from time import sleep
6
7 class Driver:
8 
9 #MAPEAMENTO DO __INIT__ PARA A LOCALIZAÇÃO DE ARQUIVOS
10 def __init__(self, cep=False, cnpj=False):
11		 directory = 'E:\\FATEC\\PI\\Files' 
12		 chrome_options = webdriver.ChromeOptions() 
13		 preferences = {"download.default_directory": directory}
14		 chrome_options.add_experimental_option("prefs", preferences)
15		 self.driver = webdriver.Chrome(chrome_options=chrome_options, executable_path='C:\\webbot\\chromedriver')
16		 self.wait = WebDriverWait(self.driver, 5)
17		 self.cep = cep
18		 self.cnpj = cnpj
19		 self.openSite()
20		 # self.driver.close()
21 
22 #FUNÇÃO QUE FARÁ O ACESSO AO SITE DE MAPA CEP E COLETARÁ DADOS DE LATITUDE E LONGITUDE DE ACORDO COM O CEP COLETADO NOS DADOS DA EMPRESA 
23 def openSite(self):
24		 self.driver.maximize_window()
25		 self.driver.get("https://www.mapacep.com.br/index.php")
26		 self.wait.until(EC.presence_of_element_located((By.ID, 'keywords')))
27		 self.driver.find_element_by_id('keywords').send_keys(self.cep)
28		 self.driver.find_element_by_xpath('/html/body/header/div[1]/div/div[2]/div/form/span/button').click()
29		 sleep(10)
30		 print(self.driver.find_element_by_xpath('/html/body/main/div[3]/div/div[1]/p').text)
31		 text = self.driver.find_element_by_xpath('/html/body/main/div[3]/div/div[1]/p').text.split('\n')
32		 # print(text)
33		 # exit()
34		 endereco = text[0]
35		 latitude = text[3].split(' ')[1]
36		 longitude = text[4].split(' ')[1]
37		 print([latitude, longitude, endereco])
38		 if self.cnpj:
39				 try:
40				 self.wait.until(EC.presence_of_element_located((By.ID, 'keywords')))
41				 self.driver.find_element_by_id('keywords').clear()
42				 self.driver.find_element_by_id('keywords').send_keys(self.cnpj[0:14])
43				 self.driver.find_element_by_xpath('/html/body/header/div[1]/div/div[2]/div/form/span/button').click()
44				 sleep(10)
45				 text_cnpj = self.driver.find_element_by_xpath('/html/body/main/div[5]/div/div[1]/p[1]').text
46				 text_cnpj = text_cnpj.split('\n')
47				 print(text_cnpj)
48				 codigo_atividade = text_cnpj[6].split(' ')[7]
49				 nome_empresarial = text_cnpj[4].split(': ')[1]
50				 descricao = text_cnpj[6].split(' ')[9:]
51				 # self.driver.close()
52				 return [latitude, longitude, endereco, codigo_atividade, nome_empresarial]
53		 except:
54				 # self.driver.close()
55				 return [latitude, longitude]
56		 # self.driver.quit()
57		 # print(endereco, latitude, longitude)
58
59 #FUNÇÃO QUE REALIZA O DOWNLOAD DO ARQUIVO CONTENDO DADOS DE EMPRESAS
60 def getArchives(self):
61 		 self.driver.get(
62		 'http://receita.economia.gov.br/orientacao/tributaria/cadastros/cadastro-nacional-de-pessoas-juridicas-cnpj/dados-publicos-cnpj')
63		 links = self.driver.find_elements_by_css_selector('a.external-link')
64		 for link in links:
65				 link.click()
66				 sleep(1)
67				 self.waitDownload()
68
69 #FUNÇÃO QUE AUXILIA NO DOWNLOAD DE ARQUIVOS CONTENDO DADOS DE EMPRESAS 	 
70 def waitDownload(self):
71		 if not self.driver.current_url.startswith("chrome://downloads"):
72				 self.driver.get("chrome://downloads/")
73				 # elemento = self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="leftSpacer"]/h1')))
74				 retorno = self.driver.execute_script("""
75				 var items = downloads.Manager.get().items_;
76				 if (items.every(e => e.state === "COMPLETE"))
77				 return items.map(e => e.fileUrl || e.file_url);
78				 else
79				 return false
80				 """)
81				 # print(retorno)
82				 count = 0
83		 while retorno == False and count < 15:
84				 sleep(1)
85				 retorno = self.driver.execute_script("""
86				 var items = downloads.Manager.get().items_;
87				 if (items.every(e => e.state === "COMPLETE"))
88				 return items.map(e => e.fileUrl || e.file_url);
89				 else
90				 return false
91				 """)
92				 count += 1
93				 # print(retorno)
94				 return
```

* Criação de banco de dados mongoDB no site da MongoDB:
	* Subimos um servidor gratuito com o banco de dados NoSQL MongoDB, onde pudemos criar nosso banco de dados lá e implementar dados para o projeto. A opção gratuita possui um limite de armazenamento, mas conseguimos da mesma forma inserir todos nossos dados.
	
![image](https://user-images.githubusercontent.com/62898187/141983822-ba312ba6-0a46-4467-8768-db59b7c4cd0b.png)
Valor até o presente momento 16/11/2021
#
