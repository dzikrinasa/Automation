file = open('text.txt')
# Read all the contents of file
print(file.read(5)) #Read n number of characters by passing parameter

#read one single line at a time readline()
# print(file.readline())
# print(file.readline())

#print line by line using 
# print("------------------------------")
# line = file.readline()
# while line!="":
#     print(line)
#     line = file.readline()

print("------------------------------")
for line in file.readlines():
    print(line)


file.close()
