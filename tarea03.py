#tarea de richard valles- esta tarea es de la secion 2 y es una tarea formativa 
#de practica para explorar phyton 
#Concatenación de Números:
#Crea dos variables numéricas.
#Combina ambas variables para formar un nuevo número y muestra el resultado.
print ("introduce dos numeros para crear uno nuevo")
num1=0
num2=0 
num3=0
print ("primero numero")
num1 = input()
print ("segundo numero")
num2 = input()
print ("ahora crearemos un numero nuevo",num1,num2)
#segundo ejercicio
print ("ahora te dare los numeros pares de una lista de numero que tu me digas")
nombre=""
print ("primero dime tu nombre")
nombre = input()
print ("hola",nombre,"bienvenido")
numero_lista = int(input("dame un numero del cual quieras saber sus numeros pares en lista"  ))
for i in range (numero_lista+1): 
    if i % 2 == 0: 
        print (i)
        
    # ahora intentare pedir el nombre del usuario y ponerselo al reves
print ("hola, dame tu nombre y te enseñare un truco")
nomborig = input()
nombrenuevo = nomborig [::-1]
print (nombrenuevo)

