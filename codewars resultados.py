Multiply
Python:

def multiply(a,b):
    return a * b

Combine strings
Python:

def combine_names (Daby, Back): 
                  return f"{Daby} {Back}" 

Switch it Up!
Python:

def switch_it_up(number):
    numbers = {
        0: "Zero" ,
        1: "One" ,
        2: "Two" ,
        3: "Three" ,
        4: "Four" ,
        5: "Five" ,
        6: "Six" ,
        7: "Seven" ,
        8: "Eight" ,
        9: "Nine" 
                }
    
    
  
    return numbers[number]


Regexp Basics - is it a digit?
Python:

def is_digit(string):
   return len(string) == 1 and string.isdigit()


Classy Classes
Python:

class Person:
    def __init__ (self, name, age): 
        self.age = age
        self.name = name
    
    @property 
    def info(self):
        return self.name + "s age is " + str(self.age)



    Find the sum of the roots of a quadratic equation
Python:

def roots(a, b, c):
    import math
    discriminante = b**2 - 4*a*c
    if discriminante < 0:
        return None
    if discriminante > 0:
        x1 = ((-b + math.sqrt(discriminante)) / (2*a))
        x2 = ((-b - math.sqrt(discriminante)) / (2*a))
        return round(x1 + x2, 2)
    if discriminante == 0:   
        raiz= -b / (2*a)
        return round (raiz + raiz,2)
        



Multiplication table for number
Python:

def multi_table(multiplicando):
    tabla_de_multiplicar = ""

    for multiplicador in range(1, 11):
        if multiplicador == 10:
            tabla_de_multiplicar += f"{multiplicador} * {multiplicando} = {multiplicador * multiplicando}"
        else:
            tabla_de_multiplicar += f"{multiplicador} * {multiplicando} = {multiplicador * multiplicando}\n"

    return tabla_de_multiplicar

         
         
         
   Scala:

def multiTable(n: Int): String = {
var multiplo = 1
var table: String=("")
while multiplo<10 do
  table+=(s"$multiplo * $n = " + multiplo * n+"\n")
  multiplo=multiplo+1
 table+=(s"$multiplo * $n = " + multiplo * n)
return(table)
}




Function 1 - hello world
Python:

def greet() :
    
     return "hello world!"
    
    #What's the plan now?😎