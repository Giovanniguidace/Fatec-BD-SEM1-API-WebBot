import os
import shutil
from Driver import *
from DataBase import *


class ArchivesPath:
    def readInChunks(self, file, size):
        while True:
            data = file.read(size)
            if not data:
                break
            yield data

    def fragArchive(self, path):
        b = 102400
        kb = b * 100
        files = os.listdir(path)
        for archives in files:
            file = open(path + '\\' + archives)
            count = 1
            for piece in self.readInChunks(file=file, size=kb):
                new = open('E:\\FATEC\\PI\\Files\\frags\\frag' + str(count) + '.txt', 'w')
                new.writelines(piece)
                new.close()
                count += 1
            os.remove(path + '\\' + archives)
            self.readerArchive()

    def readerArchive(self):
        directory = 'E:\\FATEC\\PI\\Files\\frags'
        path = os.listdir(directory)
        db = DataBase()
        for files in path:
            # print(files)
            file = open(directory + '\\' + files)
            for line in file:
                text = line.split(' ')
                c = line
                pos = text[0].find('F')
                # print(pos)
                if pos == 1:

                    # obtem o valor da cidade
                    cidade = line[688:738]
                    print(cidade)
                    # especifica por dados provinientes de são jose
                    # cidade = 'SAO JOSE DOS CAMPOS'
                    if cidade == 'SAO JOSE DOS CAMPOS                                         ' or cidade == "SAO PAULO                                         ":
                        cep = line[674:682]
                        cnpj = line[3:18]
                        nome_fantasia = line[168:223]

                        # situação cadastral
                        # 01 - NULA # 02 - ATIVA # 03 - SUSPENSA  # 04 - INAPTA  # 8 - BAIXADA
                        situacao = line[223:2]
                        data = line[225:231]
                        logadouro = line[402:462]
                        telefone = line[738:750]
                        email = line[775:924]
                        coordenadas = Driver(cep, cnpj).openSite()
                        # print(coordenadas)
                        # cria o json a ser inserido
                        try:
                            empresa = {'cnpj': cnpj, 'Fantasia': coordenadas[4], 'situacao': situacao,
                                       'data_situacao': data,
                                       'cep': cep, 'cidade': cidade, 'endereco': coordenadas[2],
                                       'latitude': coordenadas[0], 'longitude': coordenadas[1], 'codigo_atividade': coordenadas[3], }
                        except:
                            empresa = {'cnpj': cnpj,  'situacao': situacao,
                                       'data_situacao': data,
                                       'cep': cep,
                                       'latitude': coordenadas[0], 'longitude': coordenadas[1],
                                        }
                        print(empresa)
                        # exit()

                        # insere o json no banco
                        db.insertOne(empresa)

        shutil.make_archive("E:\\FATEC\\PI\\Files\\zips\\zipFrags", "zip", "E:\\FATEC\\PI\\Files\\frags")
