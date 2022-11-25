print("1).Tabla de multiplicación");
print("2).Mostrar listados de numeros impares ");
print("3).Mostrar los multiplos de un numero (1-100)");
print("4).salir");


opt= int(input("Ingrese la opción que quiere ingresar: "));

if(opt==1):
   num= int(input("Ingrese un numero entero:"));

   if num<0:
        num *= -1;

   start=int(input("Ingrese la posición inicial:"));
   end=int(input("Ingrese la posicion final :"));
   print("*****Tabla de multiplicación del ",num, "****");

   for n in range (start, end+1):
        print(num,"*",n,"=", num*n);

elif (opt==2):
    num=int(input("Ingrese  un numero  entero :"));

    print("");
    print("Lista de numeros impares del 1  al ",num);
    for i  in range (1,num,2):
        print(i);

elif(opt==3):
    num=int(input("Ingrese un numero entero :"));
    if(num<0):
        num *=-1;
        print("");
        print("Lista de numeros  multiplos de:",num,"(1-100)");
        for k in range (1,100):
            if(k%num==0):
                print(k);
else:
    print("Hasta luego")
