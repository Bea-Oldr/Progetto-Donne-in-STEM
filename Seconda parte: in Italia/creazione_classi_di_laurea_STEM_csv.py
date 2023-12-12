#programma perla creazione di classi_di_laurea_STEM, a partire da classi_di_laurea, tenere solo i dati che servono: il codice e la descrizione
#per dividere i corsi STEM nei loro ambiti è stato necessario inserire manualmente la sigla (S, T, E ed M) perchè non era possibile automatizzare tutto il processo
import csv

#letteura database con le classi di laurea
with open('classi_di_laurea.csv', 'r') as classi_file:    #l'apertura del file è fatta utilizzando with, alla fine di with si chiude anche il file 
    classi_reader = csv.reader(classi_file, delimiter=',', quotechar='"')
    classi = list(classi_reader)[1:]

stem = [['num', 'STEM', 'codice', 'descrizione']]   #sarà linsieme dei record del csv
for i in classi:
    if i[9]!='No':
        del i[3:9]
        i[0] = len(stem)+1
        if 'INGEGNERIA' in i[2].upper():    #le la descrizione ingengneria andrà in E
            i[3]='E'
        app=i[3]
        i[3]=i[2]
        i[2]=i[1]
        i[1]=app
        stem.append(i)

#tutti quelli che non sono già stati classificati vanno fatti a mano
for i in stem:
    if i[1] != 'E':
        print('inserisci la classe di STEM per ', i[3])
        i[1]= input()

#creazione classi_di_laurea.csv formato da stem
csv_file_path = 'classi_di_laurea_STEM.csv'

with open(csv_file_path, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerows(stem)

