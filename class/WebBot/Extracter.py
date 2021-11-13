import re
import os
import json
from DataBase import *

directory = 'E:\\FATEC\\PI\\Files\\frags'
path = os.listdir(directory)
db = DataBase
for files in path:
    print(files)
    file = open(directory+'\\'+files)
    for line in file:
        text = line.split(' ')
        c = line
        pos = text[0].find('F')
        # print(pos)
        if pos == 1:
            try:
                #obtem o valor da cidade
                cidade = line[688:738]

                #especifica por dados provinientes de são jose
                if cidade == 'SAO JOSE DOS CAMPOS':
                    cep = line[674:682]
                    cnpj = line[3:18]
                    nomeFantasia = line[168:223]

                    # situação cadastral
                    # 01 - NULA
                    # 02 - ATIVA
                    # 03 - SUSPENSA
                    # 04 - INAPTA
                    # 8 - BAIXADA
                    situacao = line[223:2]
                    data = line[225:231]
                    logadouro = line[402:462]
                    telefone = line[738:750]
                    email = line[775:924]

                    #cria o json a ser inserido
                    empresa = {'cnpj': cnpj, 'Fantasia': nomeFantasia, 'situacao': situacao, 'data_situacao': data,
                               'cep': cep, 'cidade': cidade, 'logadouro': logadouro, }

                    #insere o json no banco
                    db.insertOne(empresa)
            except:
                print("Não possui o dado requirido")






