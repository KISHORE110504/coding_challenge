num = 0
for i in range(1,101,1):
  num+= 1
  if num%3 == 0:
    if num%5 ==0:
      print("FizzBuzz")
    else:
      print("Fizz")
  elif num%5 ==0:
    print("Buzz")
  else:
    print(i)
   
