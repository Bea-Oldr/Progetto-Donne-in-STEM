#programma per creare il csv per creare la mappa cloropleggica dell'italia con il numero di donne laureate per regione, a partire dal csv con laureate per comune
#programma per la creazione di regioni.csv che conterrà la somma del num di laureate dall'2010 all'2022 divise per regione
import csv

#lettura database laureti per comune dall'2010 all'2015
with open('07_laureatixresidenza.csv', 'r') as laureatiITA_file:
    laureatiITA_reader = csv.reader(laureatiITA_file, delimiter=';', quotechar='"')
    laureatiITA = list(laureatiITA_reader)[1:]

laureateITA = [] #conterrà tutti i record con le laureate, i dati vengono ripuliti e di ogni record rimane la provincia e il numero
for i in laureatiITA:   #cancello tutti i record che non mi servono e tutte le colonne che non servono
    if 'F' in i:
        del i[0:2]
        del i[1:3]
        del i[1]
        laureateITA.append(i) #laureateITA contiene tutte le donne laureate e la provincia da dove vengono
regioni = [
    ['Abruzzo', 0],
    ['Basilicata', 0],
    ['Calabria', 0],
    ['Campania', 0],
    ['Emilia-romagna', 0],
    ['Friuli Venezia Giulia', 0],
    ['Lazio', 0],
    ['Liguria', 0],
    ['Lombardia', 0],
    ['Marche', 0],
    ['Molise', 0],
    ['Piemonte', 0],
    ['Puglia', 0],
    ['Sardegna', 0],
    ['Sicilia', 0],
    ['Toscana', 0],
    ['Trentino-alto adige/sudtirol', 0],
    ['Umbria', 0],
    ['Valle d\'Aosta', 0],
    ['Veneto', 0]
]       #contiene i nomi delle regioni, gli 0 è dove poi andranno aggiunti i numeri delle donne per regione

#suddivido il num di donne laureate nelle regioni
for i in laureateITA:
    if "L'AQUILA" in i or 'CHIETI' in i or 'PESCARA' in i or 'TERAMO' in i:
        regioni[0][1] += int(i[1])
    elif 'MATERA' in i or 'POTENZA' in i:
        regioni[1][1] += int(i[1])
    elif 'CATANZARO' in i or 'COSENZA' in i or 'CROTONE' in i or 'REGGIO CALABRIA' in i or 'VIBO VALENTIA' in i:
        regioni[2][1] += int(i[1])
    elif 'AVELLINO' in i or 'BENEVENTO' in i or 'CASERTA' in i or 'NAPOLI' in i or 'SALERNO' in i:
        regioni[3][1] += int(i[1])
    elif 'BOLOGNA' in i or 'FERRARA' in i or "FORLI'-CESENA" in i or 'MODENA' in i or 'PARMA' in i or 'PIACENZA' in i or 'RAVENNA' in i or 'REGGIO EMILIA' in i or 'RIMINI' in i:
        regioni[4][1] += int(i[1])
    elif 'GORIZIA' in i or 'PORDENONE' in i or 'TRIESTE' in i or 'UDINE' in i:
        regioni[5][1] += int(i[1])
    elif 'FROSINONE' in i or 'LATINA' in i or 'RIETI' in i or 'ROMA' in i or 'VITERBO' in i:
        regioni[6][1] += int(i[1])
    elif 'GENOVA' in i or 'IMPERIA' in i or 'LA SPEZIA' in i or 'SAVONA' in i:
        regioni[7][1] += int(i[1])
    elif 'BERGAMO' in i or 'BRESCIA' in i or 'COMO' in i or 'CREMONA' in i or 'LECCO' in i or 'LODI' in i or 'MANTOVA' in i or 'MILANO' in i or 'MONZA E BRIANZA' in i or 'PAVIA' in i or 'SONDRIO' in i or 'VARESE' in i:
        regioni[8][1] += int(i[1])
    elif 'ANCONA' in i or 'ASCOLI PICENO' in i or 'FERMO' in i or 'MACERATA' in i or 'PESARO E URBINO' in i:
        regioni[9][1] += int(i[1])
    elif 'CAMPOBASSO' in i or 'ISERNIA' in i:
        regioni[10][1] += int(i[1])
    elif 'ALESSANDRIA' in i or 'ASTI' in i or 'BIELLA' in i or 'CUNEO' in i or 'NOVARA' in i or 'TORINO' in i or 'VERBANO CUSIO OSSOLA' in i or 'VERCELLI' in i:
        regioni[11][1] += int(i[1])
    elif 'BARI' in i or 'BARLETTA - ANDRIA - TRANI' in i or 'BRINDISI' in i or 'FOGGIA' in i or 'LECCE' in i or 'TARANTO' in i:
        regioni[12][1] += int(i[1])
    elif 'CAGLIARI' in i or 'NUORO' in i or 'OLBIA' in i or 'ORISTANO' in i or 'SASSARI'in i:
        regioni[13][1] += int(i[1])
    elif 'AGRIGENTO' in i or 'CALTANISSETTA' in i or 'CATANIA' in i or 'ENNA' in i or 'MESSINA' in i or 'PALERMO' in i or 'RAGUSA' in i or 'TRAPANI' in i or 'SIRACUSA' in i:
        regioni[14][1] += int(i[1])
    elif 'AREZZO' in i or 'FIRENZE' in i or 'GROSSETO' in i or 'LIVORNO' in i or 'LUCCA' in i or 'MASSA CARRARA' in i or 'PISA' in i or 'PISTOIA' in i or 'PRATO' in i or 'SIENA' in i:
        regioni[15][1] += int(i[1])
    elif 'BOLZANO' in i or 'TRENTO' in i:
        regioni[16][1] += int(i[1])
    elif 'PERUGIA' in i or 'TERNI' in i:
        regioni[17][1] += int(i[1])
    elif 'AOSTA' in i:
        regioni[18][1] += int(i[1])
    elif 'BELLUNO' in i or 'PADOVA' in i or 'ROVIGO' in i or 'TREVISO' in i or 'VENEZIA' in i or 'VERONA' in i or 'VICIENZA' in i:
        regioni[19][1] += int(i[1])

#per creare il csv con i dati delle regioni 
csv_file_path = 'regioni.csv'

with open(csv_file_path, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerows(regioni)

