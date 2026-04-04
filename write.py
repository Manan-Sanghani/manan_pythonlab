# 1.write a single string

f=open("one.txt","w")
f.write("Hello students\n")
f.write("Welcome to python file handling.\n")
f.write("Learning is Fun!\n")
f.close()

# 2.old data is errased

f=open("one.txt","w")
f.write("New content only.\n")
f.close()

# 3.old data kept

f=open("one.txt","a")
f.write("This line is added at the end.\n")
f.close()

# 4.writelines

f=open("one.txt","w")
lines=[
"python programming\n",
"File handling\n",
"Error handling\n",
"Exception handling\n"
]
f.writelines(lines)
f.close()
