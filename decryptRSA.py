#Jonathan Gunter
def phi(a):
    first = a
    i=2
    while ((i*i) <= a):
        if a%i:
            i += 1
        else:
            a //= i
    b = first/a
    return ((a-1)*(int(b)-1))

def egcd(a,b):
    rOld = a
    r = b
    sOld = 1
    s = 0
    tOld = 0
    t = 1

    while ( r != 0):
        q = rOld/r
        temp = rOld
        rOld = r
        r = temp - (int(q)*r)
        temp = sOld
        sOld = s
        s = temp-(int(q)*s)
        temp = tOld
        tOld = t
        t = temp-(int(q)*t)
    return tOld;

n = int(input("Enter n"))
b = int(input("Enter b"))

factor1 = (phi(n))
modInv = (egcd(factor1,b))

if (modInv < 0):
    modInv = modInv+factor1

dKey = modInv
print("dKey : " + str(dKey))

x = bin(dKey)

file1 = open("Table5-1.txt") #Enter file with RSA ciphertext here
finalList = []
for a in file1:
    mylist = (a.split())
    for num in mylist:
        length = (len(x))
        z=1
        i=2
        while (i < length):
            z=((z*z)% n)
            if (int(x[i]) == 1):
                z = (z*int(num))%n
            i = i+1
        x1 = z%26
        x2 = (z/26)%26
        x3 = z/676
        
        final1 = chr(int(x1)+ ord('a'))
        final2 = chr(int(x2)+ ord('a'))
        final3 = chr(int(x3)+ ord('a'))

        finalList.append(final3)
        finalList.append(final2)
        finalList.append(final1)
        
fText = ""
for r in finalList:
    fText += r
    
print(fText)

        



