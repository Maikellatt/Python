# Kirjuta programm, mis ütleb, kas kasutaja poolt etteantud täisarv on paarisarv või mitte. 
# (paarisarvu mõiste - odd/even)

a = int(input('Arv: '))
if a % 2 == 0:
    print(a, 'on paarisarv:')
else:
    print(a, 'on paarituarv:')