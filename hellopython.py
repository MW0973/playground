lista=[]

for i in range(0,3):
  liczba=int(input("Podaj element: "))

  lista.append(liczba)
  

print(lista)

lista.sort()

print("Posortowana lista: ", lista)
lista2=lista
lista2.reverse()
print("Posortowana odwrotnie lista: ",lista2)
suma=sum(lista)
print("Suma: ", suma)
max=max(lista)
min=min(lista)
print("Wartosc najmniejsza to: ", min, ", a największa to: ", max)
        



