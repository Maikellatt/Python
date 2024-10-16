# Kolmnurki liigitatakse külgede pikkuse järgi erikülgseteks, võrdhaarseteks ja võrdkülgseteks. 
# Kirjutada programm, mis küsib kasutajalt kolme külje pikkused ning 
# väljastab vastusena kolmnurga liigi. 
# Lisaks tuleb kontrollida, kas etteantud küljepikkustega kolmnurk saab üldse eksisteerida. 
# Külje pikkused ei pea olema täisarvud. (ujukomaarv - float)

a = float(input('Sisesta kolmnurga esimese külg'))
b = float(input('Sisesta kolmnurga teise külg'))
c = float(input('Sisesta kolmnurga kolmas külg'))

if not (a + b > c and a + c > b and b + c > a):
    print('Kolmnurk ei saa eksisteerida')

elif a == b == c:
    print('Kolmnurk on võrdkülgne')
elif a == b or a == c or b == c:
    print('Kolmnurk on võrdhaarne')
else:
    print('Kolmnurk on erikülgne')