#creazione di 4 grafici a barre, ogniuno per un ambito delle STEM, con la differenza tra num di ragazze e ragazzi in percentuale (dall'2015 all'2020)
#((F-M)/tot)*100 se il grafico va in positivo ci sono più femmine negativo più maschi
import csv
import matplotlib.pyplot as plt

#lettura database laureti dall'2010 all'2017
with open('laureati_per_ateneo_corso_10_17.csv', 'r') as laureati_file:    
    laureati_reader = csv.reader(laureati_file, delimiter=',', quotechar='"')
    laureati_tot = list(laureati_reader)[1:]

#letteura database con le classi di laurea STEM e il loro ambito
with open('classi_di_laurea_STEM.csv', 'r') as classi_file: 
    classi_reader = csv.reader(classi_file, delimiter=';', quotechar='"')
    classi_STEM = list(classi_reader)[1:]

#prendere in considerazione solo i record dei laureati dal 2015 al 2020
laureate = []   #contiene i record che si riferiscono alle donne
laureati = []   #contiene i record che si riferiscono agli uomini
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

#prendere in considerazione solo i record dei laureati dal 2015 al 2020
for i in laureati_tot:
    if int(i[1])<=2020 and int(i[1])>=2015: 
        if i[8]=='F':
            laureate.append(i)
        else:
            laureati.append(i)

#dividere le classi di laurea nei loro ambiti
s_cod = {}  #dizionario per i corsi in S, chiave = classe di laurea, valori= [0, 0] che rappresentano [num_F, num_M], i valori effettivi verranno calcolati dopo
t_cod= {}   #dizionario per i corsi in T
e_cod = {}  #dizionario per i corsi in E
m_cod = {}  #dizionario per i corsi in M
#nella creazione dei grafici è risultato che molti corsi pur avendo classi di laurea diverse erano molto simili quindi sono stati accorpati
archi_cod=[]   #codici che nel grafico andranno sotto il nome di Architettura 
civ_cod=[]  #codici che nel grafico andranno sotto il nome di Civile (ingegneria civile)
for i in classi_STEM:
    if i[2].startswith("L") and not('abilitazione' in i[3]):
        if i[1]=='S':
            s_cod[i[2]]=[0, 0]
        elif i[1]=='T':
            t_cod[i[2]]=[0, 0]
        elif i[1]=='E':
            if 'ARCHI' in i[3].upper() or 'EDIL' in i[3].upper():
                archi_cod.append(i[2])
                e_cod['Archi']=[0, 0]
            elif 'AMBI' in i[3].upper() or  'CIVILE' in i[3].upper():
                e_cod['Civ']=[0, 0]
                civ_cod.append(i[2])
            else:
                e_cod[i[2]]=[0, 0]
        else:
            m_cod[i[2]]=[0, 0]

#somma delle laureate per codice di laurea
for i in laureate:
    if i[4] in s_cod:
        s_cod[i[4]][0] += int(i[9])
    if i[4] in t_cod:
        t_cod[i[4]][0] += int(i[9])
    if i[4] in e_cod:
        e_cod[i[4]][0] += int(i[9])
    elif i[4] in archi_cod:
        e_cod['Archi'][0] +=int(i[9])
    elif i[4] in civ_cod:
        e_cod['Civ'][0] += int(i[9])
    if i[4] in m_cod:
        m_cod[i[4]][0] += int(i[9])

#somma delli laureati per codice di laurea
for i in laureati:
    if i[4] in s_cod:
        s_cod[i[4]][1] += int(i[9])
    if i[4] in t_cod:
        t_cod[i[4]][1] += int(i[9])
    if i[4] in e_cod:
        e_cod[i[4]][1] += int(i[9])
    elif i[4] in archi_cod:
        e_cod['Archi'][1] +=int(i[9])
    elif i[4] in civ_cod:
        e_cod['Civ'][1] += int(i[9])
    if i[4] in m_cod:
        m_cod[i[4]][1] += int(i[9])



#grafico per le lauree in S
dati = {}   #chiave = nome classe, valore = differenza % tra num_F e num_M

for i in s_cod:
    tot = s_cod[i][0]+s_cod[i][1]
    dati[i]= ((s_cod[i][0]/tot)-(s_cod[i][1])/tot)*100

#per mettere il dizionario in ordine crescente di dati
dati = dict(sorted(dati.items(), key=lambda item: item[1]))
dati = dict(reversed(dati.items()))

chiavi = list(dati.keys())  #asse y
valori = list(dati.values())#asse x

plt.figure(facecolor='#EFF2FA')

#per togliere i bordi e l'asse y

ax = plt.axes()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.set_facecolor("#EFF2FA")

plt.barh(chiavi, valori, color='#DECDF4', height= 0.6)

#per mettere le etichette dell'asse x in %
plt.xticks(ticks=[-100, -75, -50, -25, -0, 25, 50, 75, 100], labels=['-100%', '-75%', '-50%', '-25%', '0', '25%', '50%', '75%', '100%'])

#togliere i valori asse y
plt.gca().axes.get_yaxis().set_visible(False)

#aggiungere etichette e titoli
plt.ylabel('Classe Laurea')
plt.title('Differenza tra numero di F e M in S', y=1.05)
plt.grid(axis='x', which='major', linestyle='--', color='gray', linewidth=0.5, alpha=0.7)

plt.show()



#grafico per le lauree in T
dati = {}   #chiave = nome classe, valore = differenza % tra num_F e num_M

for i in t_cod:
    tot = t_cod[i][0]+t_cod[i][1]
    dati[i]= ((t_cod[i][0]/tot)-(t_cod[i][1])/tot)*100

#per mettere il dizionario in ordine crescente di dati
dati = dict(sorted(dati.items(), key=lambda item: item[1]))
dati = dict(reversed(dati.items()))

chiavi = list(dati.keys())  #asse y
valori = list(dati.values())#asse x

plt.figure(facecolor='#EFF2FA')

#per togliere i bordi e l'asse y

ax = plt.axes()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.set_facecolor("#EFF2FA")

plt.barh(chiavi, valori, color='#DECDF4', height= 0.6)

#per mettere le etichette dell'asse x in %
plt.xticks(ticks=[-100, -75, -50, -25, -0, 25, 50, 75, 100], labels=['-100%', '-75%', '-50%', '-25%', '0', '25%', '50%', '75%', '100%'])

#togliere i valori asse y
plt.gca().axes.get_yaxis().set_visible(False)

#aggiungere etichette e titoli

plt.ylabel('Classe Laurea')
plt.title('Differenza tra numero di F e M in T', y=1.05)
plt.grid(axis='x', which='major', linestyle='--', color='gray', linewidth=0.5, alpha=0.7)

plt.show()



#grafico per le lauree in E
dati = {}   #chiave = nome classe, valore = differenza % tra num_F e num_M

for i in e_cod:
    tot = e_cod[i][0]+e_cod[i][1]
    dati[i]= ((e_cod[i][0]/tot)-(e_cod[i][1])/tot)*100

#per mettere il dizionario in ordine crescente di dati
dati = dict(sorted(dati.items(), key=lambda item: item[1]))
dati = dict(reversed(dati.items()))

chiavi = list(dati.keys())  #asse y
valori = list(dati.values())#asse x

plt.figure(facecolor='#EFF2FA')

#per togliere i bordi e l'asse y

ax = plt.axes()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.set_facecolor("#EFF2FA")

plt.barh(chiavi, valori, color='#DECDF4', height= 0.6)

#per mettere le etichette dell'asse x in %
plt.xticks(ticks=[-100, -75, -50, -25, -0, 25, 50, 75, 100], labels=['-100%', '-75%', '-50%', '-25%', '0', '25%', '50%', '75%', '100%'])

#togliere i valori asse y
plt.gca().axes.get_yaxis().set_visible(False)

#aggiungere etichette e titoli
plt.ylabel('Classe Laurea')
plt.title('Differenza tra numero di F e M in E', y=1.05)
plt.grid(axis='x', which='major', linestyle='--', color='gray', linewidth=0.5, alpha=0.7)

plt.show()



#grafico per le lauree in M
dati = {}   #chiave = nome classe, valore = differenza % tra num_F e num_M

for i in m_cod:
    tot = m_cod[i][0]+m_cod[i][1]
    dati[i]= ((m_cod[i][0]/tot)-(m_cod[i][1])/tot)*100

#per mettere il dizionario in ordine crescente di dati
dati = dict(sorted(dati.items(), key=lambda item: item[1]))
dati = dict(reversed(dati.items()))

chiavi = list(dati.keys())  #asse y
valori = list(dati.values())#asse x

plt.figure(facecolor='#EFF2FA')

#per togliere i bordi e l'asse y

ax = plt.axes()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.set_facecolor("#EFF2FA")

plt.barh(chiavi, valori, color='#DECDF4', height= 0.6)

#per mettere le etichette dell'asse x in %
plt.xticks(ticks=[-100, -75, -50, -25, -0, 25, 50, 75, 100], labels=['-100%', '-75%', '-50%', '-25%', '0', '25%', '50%', '75%', '100%'])

#togliere i valori asse y
plt.gca().axes.get_yaxis().set_visible(False)

#aggiungere etichette e titoli

plt.ylabel('Classe Laurea')
plt.title('Differenza tra numero di F e M in M', y=1.05)
plt.grid(axis='x', which='major', linestyle='--', color='gray', linewidth=0.5, alpha=0.7)

plt.show()
