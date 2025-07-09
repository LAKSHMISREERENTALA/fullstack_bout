with open('fifth.txt','w') as f:
    f.write("CSM")
with open('fifth.txt','a') as f:
    f.write("CSD,CSE")
with open('fifth.txt','r') as f:
    content=f.read()
    print(content)
