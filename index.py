def My_print_hello ():
    print("Hello World")
My_print_hello ()

def My_print_hello(name):
    print(name)
My_print_hello("Emma")

def Add(a,b):
    print(a+b)
Add(8,2)

def GetHello(a):
    return "Hello la plateforme"
a = "Hello la plateforme"
print(a)

def calcule(num1,operator,num2):
    if operator == "+" :
        print(num1 + num2)
    elif operator == "-":
        print(num1-num2)
    elif operator == "*":
        print(num1*num2)
    elif operator == "%":
        print(num1%num2)
    elif operator == "/":
        print(num1/num2)
    else :
        return
calcule(5,"-",6)

def nombre(num1):
    if num1 > 0 :
        print("Le nombre est positif")
    else :
        print("Le nombre est négatif")
nombre(-8)

def fonction(langage):
    if langage == "JavaScript" :
        print("Tu es un développeur web")
    elif langage == "python" :
        print("Tu es un développeur IA")
    elif langage == "java" :
        print("Tu es un développeur logiciel")
    elif langage == "reactjs" :
        print("Tu es un développeur IA")
    else :
        print("Un jour, je serais le meilleur développeur")
fonction("JavaScript")

def fonction(type,saison):
    if type == "fruits" and saison == "hiver":
        print("Orange, mandarine et kiwi")
    elif type == "fruits" and saison == "été":
        print("Poire, fraise,cassis")
    elif type == "légumes" and saison == "hiver":
        print("Carotte,topinambour,endive")
    elif type == "légumes" and saison == "été":
        print("Artichaut, aubgerine,navet")
    else :
        pass
fonction("fruits","hiver")
