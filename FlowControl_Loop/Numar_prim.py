# introduceti un numar de la tastatura si verificati daca este un numar prim

while True: #vreau sa restartez imput
    a = int(input('Introduceti valoarea lui a: '))

    if a <= 1:
        print('introduceti un numar mai mare ca 1')
    elif a == 2:
        print(a, 'este singurul numar par prim')
    else:
        for i in range(2,a):
            if (a % i) == 0:
                print(a, 'nu este numar prim')
                print(i, "*", a // i, "=", a)
                break
        else:
            print(a, 'este numar prim')
    again = input("Doriti sa introduceti un alt numar? d/n: ")
    if 'd' in again:
        continue
    else:
        print("La revedere!")
        break
    # ar trebui sa micsorez numarul de operatiuni: sa exclud numere pare>2 - interval sqrt a, maine..