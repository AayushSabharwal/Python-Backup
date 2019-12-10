f = open("file.txt", "w+")  #we open a file named file.txt
    #second parameter is file modes. w means write, and + means if the file doesnt exist create it
for i in range(10):
    f.write(input()+'\n')    #we write user input to the file 10 times.

f.close()   #we close the file since we are done writing to it

f = open("file.txt", "r")   #r means read
#text = f.read() #reads text present in the file
#print("!!", text)

#if we want to read line by line
lines = f.readlines()   #read all the lines
print(len(lines), type(lines))
for line in lines:
    print(line) #print each lie

f.close()   #we are done so we close the file