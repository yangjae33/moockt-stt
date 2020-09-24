import csv
cf = open("./data_output.csv", 'w')

writer = csv.writer(cf)
lst = []
lst.append("myname")
lst.append("11234")
writer.writerow(lst)

lst = []
lst.append("myname2")
lst.append("112342")
writer.writerow(lst)