# 1.read from source file

src=open("one.txt","r")
data=src.read()
src.close()

# 2.write to destination file

dst=open("two.txt","w")
dst.write(data)
dst.close()
print("File copied successfully.")