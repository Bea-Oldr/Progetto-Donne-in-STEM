#programma per la creazione di data_per_treemap che contiene la somma del numero di laureati divisi per M o F e per ambito, che vanno dall'2015 all'2020
import csv

#lettura database laureti dall'2010 all'2017
with open('laureati_per_ateneo_corso_10_17.csv', 'r') as laureati_file:
    laureati_reader = csv.reader(laureati_file, delimiter=',', quotechar='"')
    laureati_tot = list(laureati_reader)[1:]

classi_diz={}   #chiave = la classe di laurea, valori [num F, num M]
#tengo solo i record che riguardano i dati degli anni di interesse
for i in laureati_tot:
    if int(i[1])<=2020 and int(i[1])>=2015:
        cod =i[4]
        if classi_diz.get(cod) == None:
            classi_diz[cod]=[0,0]   
        if i[8]=='F':
            classi_diz[cod][0]+= int(i[9])
        else:
            classi_diz[cod][1]+= int(i[9])

#lettura database laureti dall'2018 all'2021
with open('laureati_per_ateneo_corso_18_21.csv', 'r') as laureati_file:    
    laureati_reader = csv.reader(laureati_file, delimiter=',', quotechar='"')
    laureati_tot = list(laureati_reader)[1:]

#tengo solo i record per gli anni che devo osservare
for i in laureati_tot:
    if int(i[1])<=2020 and int(i[1])>=2015: 
        cod =i[4]
        if classi_diz.get(cod) == None:
            classi_diz[cod]=[0,0]   
        if i[8]=='F':
            classi_diz[cod][0]+= int(i[9])
        else:
            classi_diz[cod][1]+= int(i[9])

#letteura database con le classi di laurea e il loro ambito
with open('classi_di_laurea.csv', 'r') as classi_file:    
    classi_reader = csv.reader(classi_file, delimiter=',', quotechar='"')
    classi = list(classi_reader)[1:]

ambiti={}   #chiave= nome ambito, valori= classi di laurea che ne fanno parte
ambiti_S ={}    #chiave= nome ambito, valori =[se sono stem (Sì o NO), colore sul grafico]
for i in classi:
    if ambiti.get(i[6]) == None:
        ambiti[i[6]]= [i[1]]
    else:
        ambiti[i[6]].append(i[1])
    if i[9]=='No':
        ambiti_S[i[6]]= [i[9], 'Purple']
    else:
       ambiti_S[i[6]]= [i[9], 'Blue'] 

#pulizia degli ambiti (osservando il database alcuni ambiti erano troppo specifici e li abbiamo accorpati ad altri)
canc_key=['Field unknown']
for i in ambiti:
    if 'humanities' in i:
        for j in ambiti[i]:
            ambiti['Humanities (except languages)'].append(j)
        canc_key.append(i)
    if 'eterinary' in i or 'orestry' in i:
        for j in ambiti[i]:
            ambiti['Agriculture'].append(j)
        canc_key.append(i)
    if 'mathematics' in i:
        for j in ambiti[i]:
            ambiti['Mathematics and statistics'].append(j)
        canc_key.append(i)
    if 'Manufacturing' in i:
        for j in ambiti[i]:
            ambiti['Engineering and engineering trades'].append(j)
        canc_key.append(i)
    if 'Welfare' in i:
        for j in ambiti[i]:
            ambiti['Social and behavioural sciences'].append(j)
        canc_key.append(i)

for i in canc_key:
    del ambiti[i]
    del ambiti_S[i]

#unione abiti e classi_diz
dati = {}   #chiave=nome ambito, valori= [num F, num M]

for i in ambiti:
    dati[i]=[0,0]
    for j in ambiti[i]:
        if classi_diz.get(j) != None:
            dati[i][0] += classi_diz[j][0]
            dati[i][1] += classi_diz[j][1]

#unione dati e ambiti_S
data =[['num', 'ambito', 'F', 'M', 'stem', 'color']]
num = 1
for i in dati:
    data.append([num, i, dati[i][0], dati[i][1], ambiti_S[i][0], ambiti_S[i][1]])
    num +=1

#creazione data_per_treemap.csv formato da data
csv_file_path = 'data_per_treemap.csv'

with open(csv_file_path, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',')
    csv_writer.writerows(data)
