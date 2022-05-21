A = 9+2
print (A)
9*9
EFM = "Enes Fehmi Manan"
len(EFM)
print("Enes","Fehmi","Manan", sep = "_" )
print()
"a" + "b"
"10" + 2 
a = 5
b = 10
c = a*b
c
degisken = 4
print(degisken*degisken)
a = "bu uzun bir metindir"
a[2:5]
"9" + 1
"_Python_".strip("_")
ifade = "Merhaba! "
ifade.strip("")
ifade = "1012340"
ifade = ifade + "1"
ifade.strip("1")
liste = ["Kazım","Ayşe","Fatma","Hayriye"]
liste.sort()
liste
set1 = set([5,7,9])
set2 = set([5,6,7])
 
set1.symmetric_difference(set2)
set1 = set([5,7,9])
set2 = set([5,6,7])
set1.union(set2)



liste = [10,10,20,40]
liste.clear()
liste

def kare_al(x):
    return (x**2)


kare_al(3)


def ikiye_bol(y):
    print("Girilen sayının yarısı:"+ str(y/2))
    
ikiye_bol(10)


type(3.14)
sakla = 9 
yeni_sakla = sakla*10
print(yeni_sakla)

ifade = "1012340"
ifade = ifade + "1"
ifade.strip("1")

type(4) 
"10" + 2


def harf_say(x):
    len(x)
    return(x)
 
harf_say("Merhaba!")

def islem(x):
    if (x<0):
        return "NO"
    else:
        return x*5
 
islem(2)

def islem(x):
    if (x>10):
        return "YES"
    else:
        return x*5
 
islem(4)

def mesaj():
    print("Merhaba!")
 
mesaj()

for i in ["a",11]:
    print(i)


def harf_say(x):
    return len(x)
 
harf_say("Merhaba!")


sayilar = [10,20,30,40]
 
for i in sayilar:
    if i == 30:
        break
    print(i)
    
A = []
 
for i in [1,2,3,4]:
    A.append(i)
 
A[0]

if [1,2,3,4] == 2:
    print("YES".lower())
else:
    print("NO")


A = "*A*"
if type(A) == str:
    A = A.strip("*")
    print(A)

A = 12
 
if type(A) == str:
    A = A.strip("*")
    print(A)
else:
    A = "*" + str(A) + "*"
    print(A.strip())

A = []
B = []
 
 
for i in [1,"a",12,"b"]:
    if type(i) == int:
        B.append(i)
    else:
        A.append(i)
 
A[1]


def islem(x,y):
    A = [x,y]
    return A[0] + A[1]
 
islem(1,3)


set1 = set([5,7,9])
set2 = set([5,6,7])
set1.difference(set2)

liste = ["A","B","C"]

liste.append("D")

liste

liste = [10,20,30,40]
liste.pop(1)
liste

t = ("a",10,"b")
t[0] = 1

x"set1 = set([5,7,9])
set2 = set([5,6,7])
set1.union(set2)


urun_fiyatlari = [19,29,39]
 
for i in urun_fiyatlari:
    if i >= 30:
        print(i/2)
    else:
        print(i*0)


A = "*A*"    
if type(A) == str:
    A = A.strip("*")
    print(A)

A = 12    
if type(A) == str:
    A = A.strip("*")
    print(A)    
else:
    A  = "*" + str(A) + "*"
    print(A.strip())


def harf_say(x):
    return len(x)
 
harf_say("Merhaba!")




























