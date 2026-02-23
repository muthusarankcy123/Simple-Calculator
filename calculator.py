print("~~~~~~~SIMPLE CALCULATOR~~~~~~~")
print("1.ADDITION")
print("2.SUBRACTION")
print("3.MULTIPLICATION")
print("4.DIVISION")
print("5.EXPRESSION")
choice=int(input("Enter the operation which you want(1-5):"))
match(choice):
 case 1:
  a=float(input("First value:"))
  b=float(input("Second value:"))
  Answer=a+b
  print("The ADDITION of values:",Answer)
 case 2:
  a=float(input("First value:"))
  b=float(input("Second value:"))
  Answer=a-b
  print("The SUBRACTION of 2 values:",Answer)
 case 3:
  a=float(input("First value:"))
  b=float(input("Second value:"))
  Answer=a*b
  print("The MULTIPLICATION of 2 values:",Answer)
 case 4:
  a=float(input("First value:"))
  b=float(input("Second value:"))
  Answer=a/b
  print("The DIVISION of 2 values:",Answer)
 case 5:
  a=input("Enter a Expression:")
  Answer=eval(a)
  print("The Answer of the EXPRESSION:",Answer)
 case _:
  print("Invalid choice, Enter the correct choice")