import math

print("Hello")
 person_Name = ("Atta")
 person_Email = ("attafake@gmail.com")
 person_Password = (123321)
 peson_Bill = (22.99)
 person_Consistency = (False)
 print(f"How are you : {person_Name}")
 print(f"your email is : {person_Email}")
 print(f"your password is : {person_Password}")
 print(f"your bill is : RS.{peson_Bill}")
 if person_Consistency:
     print("U are a consistent customer")
 else:
     print("U are not a consistent customer")

 name = "Jhon"
 phone_Number = 3202004413
 admin = True
 percentage = 78.56

 print(int(percentage))    

 
 name = input("Name kya hai ladle? ")
 print(f"gel main aja {name} ladle")

 ask = input("ao gi gel main? (yes/no): ")

 if ask.lower() == "yes":
     print("aja ladli")
 elif ask.lower() == "no":
     print("nahi aa")
 else:
     print("samajh nahi aaya, yes ya no likho.")







lenght = float(input("Enter length"+ " "))
width = float(input("Enter width"+ " "))
unit = input("Enter unit"+ " ")
area_Of_Rectangle = lenght*width
print(f"area of rectangle is {area_Of_Rectangle}{unit}²")


item =input("what do u want"+" ")
quantity = int(input("How much do you want of it: "+" " ))
price = float(input("what is the price:"+" "))
total = price*quantity

print(f"you have bought {quantity}, {item}")
print(f"total is: Rs.{total}")



x = 3.16
y = 4 
z = 8

# result = round(x)
# result = abs(y)
# result = max(x,z,y)
# result = pow(y,3)
result = min(x,z,y)
print(result)
x = 4.3

print(math.pi)
print(math.e)

result = math.sqrt(x)
result = math.ceil(x)
result = math.floor(x)

print(result)


radius = float(input("Enter radius of the circle"+ " "))
unit = input("Enter unit"+ " ")
result = 2*math.pi*radius
print(f"the radius is {radius}")

print(f"The circumference of the circle you gave radius of is : {round(result , 2)}{unit}")





new 



a =  float(input("Enter a side A :"+ " "))
b =  float(input("ENter a side B :"+ " "))

c = math.sqrt(pow(a,2)+pow(b,2))

print(f"This is the hypotenuse of the triangle {round(c,2)}")


elif and if and else


name = input("Enter your name moti")

if name == "" :
    print("you did not type your name moti")

else:
    print(f"SO, your name is {name} moti pucha kisne name tum se kachre se ayi hu kchri abe chl nikal moti")


calculator

operator = input("Enter an operator (+, -, / ,*)")

num1 = float(input("Enter first number?" +" "))
num2 = float(input("Enter the Second number ?" +" "))


if operator == "+" :
    result = num1 + num2 
    print(f"sum of numbers is {round(result, 2)}")
elif operator == "-" :
    result = num1 - num2 
    print(f"sum of numbers is {round(result, 2)}")
elif operator == "/" :
    result = num1 / num2 
    print(f"sum of numbers is {round(result, 2)}")
elif operator == "*" :
    result = num1 * num2 
    print(f"sum of numbers is {round(result, 2)}")

else  :
    print(f"{operator} is not an operator")


Temperature


user_Role = "Admin"
age = 18
page = "Separate level hai app ka tpo" if user_Role == "Admin" else "abe chl be"

status = "Get merried  already" if age >= 18 else "Shutup you are a children"
print (status)