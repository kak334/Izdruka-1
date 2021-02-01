#1 uzd
def findLen(str):
    counter = 0
    for i in str:
        counter += 1
    return counter
str = input("Ievadi teikumu")
print(findLen(str))