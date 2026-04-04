# 1.read method

f=open("one.txt","r")
data=f.read()
print("File content: ",data)
f.close()


# 2.read one line

f=open("one.txt","r")
line1=f.readline()
line2=f.readline()
line3=f.readline()
print("line 1: ",line1)
print("line 2: ",line2)
print("line 3: ",line3)
f.close()


# 3.read all lines into a list

f=open("one.txt","r")
lines=f.readlines()
print("list of lines : ",lines)
print("number of lines : ",len(lines))
f.close()


#4. reads specific line in file

f=open("one.txt","r")
lines=f.readlines()
print(lines[2].strip())
f.close()