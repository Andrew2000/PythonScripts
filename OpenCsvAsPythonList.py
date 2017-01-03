import csv

c_reader = csv.reader(open('CA1.csv', 'r', encoding='latin-1'), delimiter=',')

ChildAccounts = [x[5] for x in c_reader][1:]

print(ChildAccounts)