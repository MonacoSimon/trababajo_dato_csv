import csv
archivo = '/home/maquina6/Escritorio/Practica3/Tp_final_ayed3_/data.csv'
with open(archivo, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    writer = csv.writer(csvfile)
    writer.writerows(csvfile)
    for row in reader:
         print(row['name'], row['country'])
         writer.writerows(['name'])