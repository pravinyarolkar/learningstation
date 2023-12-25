import csv

csv_file = open('C:\\Users\\YarolkarPravin\\src\\learningstation\\python\\src\\Notebooks\\Complete-Python-3-Bootcamp\\15-PDFs-and-Spreadsheets\\Example.csv', 'r', encoding='utf-8')

csv_data = csv.reader(csv_file)

data = list(csv_data)

print(len(data))
count = (len(data) - 1)

# print(data[:5])
'''
[['id', 'first_name', 'last_name', 'email', 'gender', 'ip_address', 'city'], 
['1', 'Joseph', 'Zaniolini', 'jzaniolini0@simplemachines.org', 'Male', '163.168.68.132', 'Pedro Leopoldo'], 
['2', 'Freida', 'Drillingcourt', 'fdrillingcourt1@umich.edu', 'Female', '97.212.102.79', 'Buri'], 
['3', 'Nanni', 'Herity', 'nherity2@statcounter.com', 'Female', '145.151.178.98', 'Claver'], 
['4', 'Orazio', 'Frayling', 'ofrayling3@economist.com', 'Male', '25.199.143.143', 'Kungur']]
'''

print(data[10])
# read from cloumn name
# ['10', 'Hyatt', 'Gasquoine', 'hgasquoine9@google.ru', 'Male', '221.155.106.39', 'Złoty Stok']

print(data[10][3])
# hgasquoine9@google.ru

all_emails = []
for num in range(count):
    all_emails.append(data[num][3])

print(all_emails)

# full names

print(data[1])
full_names = []
for line in data[1:]:
    full_names.append(line[1]+' '+line[2])
print(full_names)

import os
print(os.getcwd())

file_to_out = open('full_names.csv', mode='w', newline='')
csv_writer = csv.writer(file_to_out, delimiter=',')
csv_writer.writerow(['A','B','C'])
csv_writer.writerows([['1','2','3'],['4','5','6']]) # columns should match
file_to_out.close()
