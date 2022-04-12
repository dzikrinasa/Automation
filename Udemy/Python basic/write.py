# read the file and store all the line in list
# reverse the list
# write the list back to the list 


with open('text.txt', 'r') as reader:
    content = reader.readlines()
    reversed(content)
    with open('text.txt','w') as writer:
        for line in reversed(content):
            writer.write(line)