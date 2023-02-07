#!/usr/bin/env python3

def fibonancci(number):

  auxiliar = 0
  fi1 = 1
  fi2 = 1
  cont = 1
  while(cont <= number):
    auxiliar = fi2
    fi2 += fi1
    fi1 = auxiliar
    cont += 1

  return fi1

maxvalue = int(input("valor máximo que no superan los términos: "))
suma = 0
i = 1
while(fibonancci(i) < maxvalue):
  if(fibonancci(i)%2 == 0):
      suma += fibonancci(i)
  i += 1

print(suma)
