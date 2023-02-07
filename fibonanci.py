
#!/usr/bin/env python3

i=int(input(":"))
auxiliar = 0
fi1 = 1
fi2 = 1
cont = 1
while(cont <= i):
  auxiliar = fi2
  fi2 += fi1
  fi1 = auxiliar
  cont += 1
  print(fi1)


