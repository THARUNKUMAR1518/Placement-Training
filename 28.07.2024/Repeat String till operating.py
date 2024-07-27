test_string = "tharunkumar"
K = 30
print("The original string : " + str(test_string))
res = (test_string * (K//len(test_string) + 1))[:K]
print("String after performing repetition : " + res)
