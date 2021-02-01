def cmp1 (text,key):
    a = len(text)
    b = len(key)
    return a//b

def main ():

   
    text = input("Enter your text : ")
    key = input("Enter key : ")

    a = 0
    Result = ""

   
    if len(key) > len (text):
        cmp2 = len(key) - len(text) 
        key = key[:-cmp2 ]
    else:
        reiz = cmp1(text,key)
        key = key * reiz 
        while len(key) != len(text):
            key += key[a]
            a +=1

    
    for i in range(len(text)):
        tmp = ord(key[i]) - 96
        Result += chr( ord(text[i])+ tmp )


    print("text : ",text)
    print("Key : ",key)
    print("Result : ",Result)

main()