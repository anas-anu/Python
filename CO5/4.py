import pandas as panda
rs=panda.read_csv("studentdetails.csv",usecols=["Student Name","Roll No","Grade"])
#re=panda.read_csv("Financial Sample.csv")
print(rs)
'''First 5 Datas
print(re.head())'''


'''Last 5 Datas
print(re.tail())'''


''''
particular columns
print(re[["Country"," Profit "]])'''