import re

def regex(text):
    lst = []
    compile = re.compile("\(\d{3}\)[-.\s]?\d{3}[-.\s]?\d{4}")
    patterns = compile.finditer(text)
    
    for match in patterns:
        lst.append(match)
        print(lst)
regex("Please contact info@example.com for assistance. Phone: (123) 456-7890 or (111) 222-3333")
    
def email(text):
    compile = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+.[a-zA-Z]{2,}')
    patterns = compile.finditer(text)
    
    for match in patterns:
        print(match)

email("Please contact info@example.com for assistance. Phone: (123) 456-7890 or (111) 222-3333")

def replace(text, replacement):
    rep = regex(text)
    for num in rep:
        nums = text.replace(num, replacement)
    print(f"Please contact {nums} for assistance")
text = "Please contact info@example.com for assistance. Phone: (123) 456-7890 or (111) 222-3333"
num = "(123) 456-7890 "

replace(text, num)