#creazione di diagrammi circolari per confrontare il numero di donne e uomini laureati nelle varie categorie delle STEM, vengono presi in considerazone solo i laureati dall'2015 all'2020
import csv
import matplotlib.pyplot as plt

#lettura database laureti dall'2010 all'2017
with open('laureati_per_ateneo_corso_10_17.csv', 'r') as laureati_file:    
    laureati_reader = csv.reader(laureati_file, delimiter=',', quotechar='"')
    laureati_tot = list(laureati_reader)[1:]

laureate = [] #record laureate FEMMINE
laureati = [] #record laureati MASCHI
#tenere solo i record che riguardano i dati degli anni che ci interessano
for i in laureati_tot:
    if int(i[1])<=2020 and int(i[1])>=2015:
        if i[8]=='F':
            laureate.append(i)
        else:
            laureati.append(i)

#lettura database laureti dall'2018 all'2021
with open('laureati_per_ateneo_corso_18_21.csv', 'r') as laureati_file:    
    laureati_reader = csv.reader(laureati_file, delimiter=',', quotechar='"')
    laureati_tot = list(laureati_reader)[1:]

#tenere solo i record per gli anni che devo osservare
for i in laureati_tot:
    if int(i[1])<=2020 and int(i[1])>=2015: 
        if i[8]=='F':
            laureate.append(i)
        else:
            laureati.append(i)

#lettura database codici classi di laurea STEM
with open('classi_di_laurea_STEM.csv', 'r') as classi_file: 
    classi_reader = csv.reader(classi_file, delimiter=';', quotechar='"')
    classi_STEM = list(classi_reader)[1:]

s_cod = []  #conterrà i codici di tutte le lauree S
t_cod= [] #conterrà i codici di tutte le lauree T
e_cod = [] #conterrà i codici di tutte le lauree E
m_cod = [] #conterrà i codici di tutte le lauree M
#divisione di tutte le classi di laurea nelle proprie categorie
for i in classi_STEM:
    if i[1]=='S':
        s_cod.append(i[2])
    elif i[1]=='T':
        t_cod.append(i[2])
    elif i[1]=='E':
        e_cod.append(i[2])
    else:
        m_cod.append(i[2])
s_num=[0, 0]    #primo numero laureate, 2° laureati
t_num=[0, 0]
e_num=[0, 0]
m_num=[0, 0]
#aggiungere il numero delle laureate nelle varie categorie
for i in laureate:
    if i[4] in s_cod:
        s_num[0] += int(i[9])
    if i[4] in t_cod:
        t_num[0] += int(i[9])
    if i[4] in e_cod:
        e_num[0] += int(i[9])
    if i[4] in m_cod:
        m_num[0] += int(i[9])

#aggiungere il numero dei laureati nelle varie categorie
for i in laureati:
    if i[4] in s_cod:
        s_num[1] += int(i[9])
    if i[4] in t_cod:
        t_num[1] += int(i[9])
    if i[4] in e_cod:
        e_num[1] += int(i[9])
    if i[4] in m_cod:
        m_num[1] += int(i[9])

#creare i labels e i valori per S
labels_s = ['F', 'M']
valori_s = [s_num[0], s_num[1]]

#creare i labels e i valori per T 
labels_t = ['F', 'M']
valori_t = [t_num[0], t_num[1]]

#creare i labels e i valori per E 
labels_e = ['F', 'M']
valori_e = [e_num[0], e_num[1]]

#creare i labels e i valori per M 
labels_m = ['F', 'M']
valori_m = [m_num[0], m_num[1]]


#creare una figura con quattro subplot
fig, axs = plt.subplots(2, 2, figsize=(10, 4), facecolor='#EFF2FA')

#Primo grafico a torta
axs[0, 0].pie(valori_s, labels=labels_s, startangle=90, labeldistance=0.40, colors=["#FFADBA","#B6CBE2"])
axs[0, 0].set_title('S')

#Secondo grafico a torta
axs[0, 1].pie(valori_t, labels=labels_t, startangle=90, labeldistance=0.40, colors=['#FFADBA', '#B6CBE2'])
axs[0, 1].set_title('T')

#Terzo grafico a torta
axs[1, 0].pie(valori_e, labels=labels_e, startangle=90, labeldistance=0.40, colors=['#FFADBA', '#B6CBE2'])
axs[1, 0].set_title('E')

#Quarti grafico a torta
axs[1, 1].pie(valori_m, labels=labels_m, startangle=90, labeldistance=0.40, colors=['#FFADBA', '#B6CBE2'])
axs[1, 1].set_title('M')

plt.tight_layout()
plt.show()