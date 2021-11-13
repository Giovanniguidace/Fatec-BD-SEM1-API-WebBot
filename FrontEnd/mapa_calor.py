import pymongo
import folium

from folium import plugins

from pymongo import MongoClient

db = MongoClient('mongodb+srv://admin:admin@cluster0-vuh1j.azure.mongodb.net/test?retryWrites=true&w=majority')
db = db.get_database('BD_EMPRESAS')

collection = db.empresas

latitude = []
longitude = []
qtd_range = []
coordenadas = []
latitude = db.get_collection('empresas').distinct("latitude")
qtd_range = len(latitude)
longitude = db.get_collection('empresas').distinct("longitude")


mapa = folium.Map(location=[-23.4795233,-46.2698754],zoom_start=9)

for i in range(qtd_range):

    coordenadas.append([latitude[i],longitude[i]])
    mapa.add_child(plugins.HeatMap(coordenadas))

mapa.save("mapa_calor.html")