import csv
csv_file0=open('studentdetails.csv','r')
csv_reader=csv.reader(csv_file0)
for line in csv_reader:
    #print(line[0])
    print(line)
