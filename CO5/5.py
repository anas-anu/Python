import csv
time=[{'Days':1,'Experience':'Good','Time':8},{'Days':2,'Experience':'Good','Time':8},{'Days':3,'Experience':'Good','Time':8},{'Days':4,'Experience':'Bad','Time':6}]
csv_file=open("New.csv","w")
field_names=list(time[0].keys())
writer=csv.DictWriter(csv_file,fieldnames=field_names)
writer.writeheader()
writer.writerows(time)
csv_file.close()
csv_file=open("New.csv","r")
csv_reader=csv.reader(csv_file)
for line in csv_file:
    print(line,end="")