import re 
patterns = ['tem1', 'tem2']
text = 'This is a text in tem1'
for pattern in patterns:
    print("I am searching for", pattern)
    if re.search(pattern,text):
        print("MATCH!")
    else: print('NOT MATCH!!')