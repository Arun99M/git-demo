file = open('test.text')
#Read all the contents of file
#Read n number of characteres by passing parameters
#print(file.read(6))
#read one single line at a time readline()
#print(file.readline())
#print(file.readline())

#file.close()

#print ALl line by using readline method

line = file.readline()
while line !="":   #this is while loop
    print(line)
    line = file.readline()

#values = ( Hi, how are you)
for line in file.readlines():    #this for loop
    print(line)



























