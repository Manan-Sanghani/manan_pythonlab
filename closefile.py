# 1.manual closing

f=open("one.txt","r")

# 2.using with statement

with open("one.txt","r") as f:
    content=f.read()
    print(content)