# List is data type that allows multiple values and can be defferent data types

values = [1, 2, "jack", 4, 5]

print(values[0]) # 1

print(values[3]) # 4
print(values[-1]) # 5
print(values[1:3]) # 2 jack
values.insert(3,"bogey") # [1, 2, 'jack', 'bogey', 4, 5]
print(values)
values.append("end") # [1, 2, 'jack', 'bogey', 4, 5, 'end']
print(values)

values[2] = "JACKSON" #Updating

del values[0] #deleting

print(values)

# Tuple - same as LIST Data type but immutable
val = (1, 2, "tuple", 4.5)

print(val[1])

#val[2] = "TUPLES"

#print(val)

# Dictionary
dic = {"a":2, 4:"bcd", "c":"Hello world"}

print(dic[4])
print(dic["c"])

#
dict = {}

dict["firstname"] = "John"

dict["lastname"] = "Doe"

dict["gender"] = "Male"

print(dict)
print(dict["lastname"])