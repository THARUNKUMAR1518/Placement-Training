import re 

test_str = 'geeksforgeeks is best for geeks'
print("The original string is : " + str(test_str)) 
sub_str = '..st'
temp = re.compile(sub_str) 
res = temp.search(test_str) 
print("The substring match is : " + str(res.group(0))) 
