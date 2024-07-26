import re

def exsymbols(text):
    symbols = re.findall(r'[^\w\s]', text)
    return ''.join(symbols)
text =input ("Enter the string:")
symbols = exsymbols(text)
print(symbols)

