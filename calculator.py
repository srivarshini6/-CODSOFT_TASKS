
def calaculator ():
  while True:
  print("smiple calaculation")
  print("1.Addition +")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("5.excit")
choice=input ("enter choice (1/2/3/4/5):")
if choice == '5':
print("thanks for using the calalulator ! good bye ")
break
if choice in ('1', '2', '3', '4'):
num1=float(input("enter the frist number:"))
num2=float(input("enter the second number:"))
ifchoice == '1':
print(f"result:{num1} + {num2}={num1+num2}")
elif choice == '2':
print(f"result:{num1}-{num2}={num1-num2}")
elif choice == '3':
print(f"result:{num1}*{num2}={num1*num2}")
elif choice == '4':
if num2!= 0:
  print (f"result: {num1}/{num2}={num1/num2}")
  else :
  print("error: Divison by Zero is not allowed")
else:
print("invalid check you the option 1 to 5 ")
calaculator()
