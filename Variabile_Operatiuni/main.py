from Constructor import printMultumiri #aduc din Constructor doar ce-mi trebuie
from Constructor import randLiber #am facut asa un rand liber pentru exercitiu
from Culori import culoareText, atributeText, reset #aduc din Culori culorile cu care m-am jucat intr-o lista

#Variabile - Tipuri de date: String - caractere / int - integer/ boolean / float/double - numar zecimal / char - un carater(Java)
#Operatori:
#ARITMETICI: +, -, *, /, % (modulo - restul impartirii), // (impartirea fara zecimale). ** (la puterea)
#De COMPARARE: ==, >, <, >=, <=, != (diferit)
#introduc doi termeni de la tastatura
#LOGICI: and, or, not

print(culoareText[0] + 'CAPITOL - TIPURI DE OPERATORI' + reset[0])
print('Executam operatiuni!')
print('===============================')

a = int(input('Introduceti valoarea lui a: '))
b = int(input('Introduceti valoarea lui b: '))
randLiber()

#arat ce s-a introdus
printMultumiri()
print(culoareText[0] + 'Ati introdus valorile:', culoareText[5] + '', a, culoareText[0] + 'si: ', culoareText[5] + '', b, reset[0])
randLiber()

#fac operatiunile aritmetice
print(atributeText[1] + 'Operatorii Aritmetici:'.upper(), reset [0])

print('+ Adunare: a + b => ', a, '+', b, '=',  a + b)
print('- Scadere: a - b => ', a, '-', b, '=', a - b)
print('* Inmultire: a * b = ', a, '*', b, '=', a * b)
print('/ Impartire: a / b = ', a, '/', b, '=', float (a / b)) #float: pentru a fi sigur ca primesc zecimale desi nu era obligatoriu cred
print('% Modulo (rest / ): a % b = ', a, '%', b, '=', a % b)
print('// Partea intreaga din impartire a / b = ', a, '/', b, '=', a // b)
print('** Puterea: a^b = ', a, '^', b, '=', a ** b)
randLiber()

print(atributeText[1] + 'Operatorii De Comparare:'.upper(), reset [0])
print('> Mai mare: a > b => ', a, '>', b, '=>',  a > b)
print('< Mai mic: a < b => ', a, '<', b, '=>',  a < b)
print('== Egal: a = b => ', a, '=', b, '=>',  a == b)
print('>= Mai mare sau egal: a >= b => ', a, '>=', b, '=>',  a >= b)
print('<= Mai mic sau egal: a <= b => ', a, '<=', b, '=>',  a <= b)
print('!= Diferit: a != b => ', a, '!=', b, '=>',  a != b)
randLiber()

print(atributeText[1] + 'Operatorii Logici:'.upper(), reset [0])
print('OBS: vom introduce si variabila c pentru comparare')
c = int(input('Introduceti valoarea lui c: '))
print('AND: a > c and b > c => ', a, '>', c, 'and', b, '>', c, '=>',  a > c and b > c)
if (a > c or b > c):
    print('OR: a > c or b > c => ', a,'>', c, 'or', b, '>', c, '=>',  True)
else: print('OR: a > or b > c => ', a,'>', c, 'or', b, '>', c, '=>', False)
print('NOT: not a = b => ', 'not', a, '==', b, '=>', not a == b)
