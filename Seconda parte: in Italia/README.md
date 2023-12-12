Questi programmi e dataset servono per creare i grafici della presentazione dalla slide 13 in poi;  (numero delle slide = pagina del pdf in \Presentazione\DonneNelleSTEM.pdf)
# Database
Dal sito del miur https://dati-ustat.mur.gov.it/organization/miur sono stati presi i dataset

- 07_laureatixresidenza
- classi_di_laurea.csv
- laureati_per_ateneo_corso_10_17.csv
- laureati_per_ateneo_corso_18_21.csv

Altri dataset sono stati creati da dei programmi che abbiamo creato
- classi_di_laurea_STEM.csv
- data_per_treemap.csv
- regioni.csv

# Programmi
Ogni programma è commentato con una spiegazione di cosa produce e del come.
Alcuni sono serviti per creare i grafici che si trovano nella presentazione
- corsi_piu_freq.py ----> slide 17, 20, 23, 26
- grafici_a_torta_STEM.py ----> slide 16, 19, 22, 25

Altri programmi creano alcuni dataset
- creazione_classi_di_laurea_STEM_csv.py
- creazione_data_per_treemap_csv.py
- creazione_regioni_csv.py

Dei grafici non è stato possibile crearli in python quindi abbiamo dovuto usare dei siti
- Slide 13: nelle librerie di python per creare le mappe cloroplete non esisteva la cartina dell'Italia suddivisa per regioni quindi l'abbiamo creata utilizzando il sito: https://app.everviz.com/create?editor=wiz&panel=map_type&type=choropleth&maps, aggiungendoci la mappa: italy-with-regions_1458.geojson e il dataset regioni.csv
- Slide 14: dopo aver creato il file data_per_treemap.csv abbiamo usato il sito https://flourish.studio/ per creare le 2 treemap
