

ItemsInCart = 0
#2 items will be added to cart

if ItemsInCart != 2:
    pass #raise Exception("Products card count not matching")

assert(ItemsInCart == 0)

#try , catch

try:
    with open('text.txt', 'r') as reader:
        reader.read()

except:
    print("Some how i reached this block because there is failure in try block")

try:
    with open('text.txt', 'r') as reader:
        reader.read()

except Exception as e:
    print(e)

finally:
    print('cleaning up records')