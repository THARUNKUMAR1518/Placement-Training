import csv 

with open('sample.csv', 'r') as read_obj:  
	csv_reader = csv.reader(read_obj) 
	list_of_csv = list(csv_reader) 

	print(list_of_csv) 
