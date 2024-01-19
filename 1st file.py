history=[]
def calc( operator,x,y):
  if operator == '+':
    return x + y
  elif operator == '-':
    return x - y
  elif operator == '*':
    return x * y
  elif operator == '/':
    return x / y
  else:
    return "Invalid operator"

while True:
  print("Welcome to the calculater")
  a = input("Enter the first number: ")
  b = input("Enter the second number: ")
  op = input("Enter operator: ")
  output = calc(op,int(a),int(b))
  print(output)
  exp=str(a)+str(op)+str(b)+str("=")+str(output)
  print(exp)
  history.append(exp)
  choice=(input("if you want to continue the calculation type yes or no: "))
  if choice=="no":
      break
  previous=print(input("if you want to view history type yes or no"))
  if previous=="yes":
      print("history:")
      for enter in history:
          print(enter)
  
  
        
  
  
  
