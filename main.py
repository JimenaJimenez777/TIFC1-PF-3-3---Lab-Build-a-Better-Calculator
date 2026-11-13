def main():
  print("Bienvenido a la calculadora")
  print("opción 1 (addmultiplenumbers)")
  print("opción 2 (multiplymultiplenumbers)")
  print("opción 3 (isiteven)")
  print("opción 4 (isitaninteger)")
  Opcion=input("ingrese el número de opción: " )

  if Opcion == ["1","2","3","4"]:
    if Opcion=="1" or Opcion== "2":
        numeros = []
        continuar="s"
        while continuar=="s":
          numero=float (input("ingrese un número"))
          numeros.append(numero)
          continuar=input("¿ingresar otro número?: s/n " )
        if Opcion=="1":
          print (addmultiplenumbers(numeros))
        else:
          print (multiplymultiplenumbers(numeros))
    else:
        if Opcion=="3":
          print(isiteven( float(input("ingrese un numero"))))
        else:
          print(isitaninteger( float(input("ingrese un numero"))))
  else: print("Opción No Válida")



def addmultiplenumbers(numeros:list[float]):
  total= 0
  for number in numeros:
    total=total+number
  return total

def multiplymultiplenumbers(numeros:list[float]):
  total= 1
  for number in numeros:
    total=total*number
  return total

def isiteven(number:float):
  return number%2==0

def isitaninteger(number:float):
  return number%1==0


if __name__=="__main__":
  main()