l1 = [4, 2, 13, 21, 5] 
l2 = [] 
for i in l1: 
	temp=lambda i:i**2
	l2.append(temp(i)) 
print(l2)
