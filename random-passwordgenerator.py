import random

def pos():
    o=True
    while o:
        p=random.randint(0,char-1)
        if resultlist[p]==' ':
            resultlist.pop(p)
            resultlist.insert(int(p),a)
            o=False
        
def result():
    r=''
    for z in resultlist:
        r=r+z
    return r
    
print('[GENERATE PASSWORD OF ANY LENGTH INCLUDING UPPER CASE, LOWER CASE, DIGIT AND SPECIAL CHARACTERS]')
print('')
resultlist=[]
c=True
while c:
    char=int(input('Enter Length of the Password:'))
    print('')
    for ch in range(char):
        resultlist.append(' ')
    up=int(input('Enter no of Upper Case:'))
    print('')
    low=int(input('Enter no of Lower Case:'))
    print('')
    dig=int(input('Enter number of Digits:'))
    print('')
    sc=int(input('Enter no of Special Characters:'))
    if char>=up+low+sc+dig:
        uplist=['Q', 'A', 'Z', 'X', 'S', 'W', 'E', 'D', 'C', 'V', 'F', 'R', 'T', 'G', 'B', 'N', 'H', 'Y', 'U', 'J', 'M', 'K', 'I', 'O', 'L', 'P']
        lowlist=['q', 'a', 'z', 'x', 's', 'w', 'e', 'd', 'c', 'v', 'f', 'r', 't', 'g', 'b', 'n', 'h', 'y', 'u', 'j', 'm', 'k', 'i', 'o', 'l', 'p']
        digitlist=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        sclist=['!', '@', '#', '$', '%', '^', '&', '*','_', '-', '?', '.']
        randomlist=['Q', 'A', 'Z', 'X', 'S', 'W', 'E', 'D', 'C', 'V', 'F', 'R', 'T', 'G', 'B', 'N', 'H', 'Y', 'U', 'J', 'M', 'K', 'I', 'O', 'L', 'P', 'q', 'a', 'z', 'x', 's', 'w', 'e', 'd', 'c', 'v', 'f', 'r', 't', 'g', 'b', 'n', 'h', 'y', 'u', 'j', 'm', 'k', 'i', 'o', 'l', 'p', '!', '@', '#', '$', '%', '^', '&', '*','_', '-', '?', '.','0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        for x in range(up):
            a=random.choice(uplist)
            pos()
        for x in range(low):
            a=random.choice(lowlist)
            pos()
        for x in range(sc):
            a=random.choice(sclist)
            pos()
        for x in range(dig):
            a=random.choice(digitlist)
            pos()
        f=char-(up+low+sc+dig)
        for x in range(f):
            a=random.choice(randomlist)
            pos()
        r=result()
        print('')
        print('Password Generated |  ',r,'  |')
        c=False
    else:
        print('The number of characters you selected was(',char,')')
        print('')
        continue
    
