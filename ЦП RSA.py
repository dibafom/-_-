import math
mm=[]
def inv(a, n):
    for t in range(100):
        a1 = (1 + (n * t)) // a
        if (a * a1) % n == 1:
            return a1

p = int(input ())
q = int(input ())
n=p*q
ii=0
n1=((p-1)*(q-1))
while ii!=1:
    k=int(input("введите Ключ"))
    if (math.gcd(k,((p-1)*(q-1)))==1) and 1<k and k<n1:
        ii=1
    else:
        print("Заново")
k1=inv(k,n1)
print (k1)
m=0
mas = str(input("введите сообщение"))
for i in mas:
    if i!= ' ':
        m1 =int((ord(i.lower()) - 1071))
        mm.append (m1)
print (mm)
print (" ")
m=0
for i in mm:
    m=(m^i**k%n) % n
    print (m)
print (m)

s=(m**k1)%n
print ("Значение S:",s)

m11=(s**k)%n
print ("М11:  ", m11)

m1=0
for i in mm:
    m1=(m1^i**k%n) % n
    print ("М1:  ",m1)

if (m1==m11):
    print ("Все гууд")
else:
    print ("Чет не то")
