import pymongo
import folium



from pymongo import MongoClient

db = MongoClient('mongodb+srv://admin:admin@cluster0-vuh1j.azure.mongodb.net/test?retryWrites=true&w=majority')
db = db.get_database('BD_EMPRESAS')

collection = db.empresas


cnpj = []
latitude = []
longitude = []
qtd_range = []
endereco = []

cnpj = db.get_collection('empresas').distinct("cnpj")
latitude = db.get_collection('empresas').distinct("latitude")
qtd_range = len(latitude)
longitude = db.get_collection('empresas').distinct("longitude")
endereco = db.get_collection('empresas').distinct("endereco")

mapa = folium.Map(location=[-23.4795233,-46.2698754],zoom_start=9)

for i in range(qtd_range):

    folium.Marker([latitude[i], longitude[i]], popup='CNPJ: '+cnpj[i]+'\n Endereco: '+endereco[i]).add_to(mapa)


mapa.save("index.html")