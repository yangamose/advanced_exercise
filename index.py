a = 5
b = 10
c = 7

a += 3
b *= 2
c %= 4

import math
result = math.sqrt(a**2 + b**2 + c**2)
print(f"final result: {round(result, 2)}")

x = int(input("enter an intiger for x:"))
y = int(input("enter an intiger for y;"))
z = int(input("enter an intiger for z:"))
is_even = (x % 2 == 0)
is_positive = (y > 0)
is_in_range = (10 <= z <= 50)
final_condition = is_even and is_positive and is_in_range
print(f"final condition: {final_condition}")

score = float(input("enter your score:"))
score += 5
score -= 10
score = (max(0,min(100,score)))
if score >=90:
   grade = "A"
elif score >=80:
   grade = "B"
elif score >=70:
   grade = "C"
elif score >=60:
   grade = "D"
else:
   grade = "F"
print(f"your final score is:{score},and your grade is:{grade}")

num1 = int(input("enter first number:"))
num2 = int(input("enter second number:"))
operation = input("enter operation(+, -, *, /):")
if operation == "+":
   result = num1 + num2 
elif operation == "-":
   result = num1 - num2
elif operation == "*":
   result = num1 * num2
elif operation == "/":
   if num2 != 0:
      result = num1 / num2
   else:
    result = "error: division by zero is not allowed."
print(f"result: {result}")