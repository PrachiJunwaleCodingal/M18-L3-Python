#Armstrong number
num = int(input("Enter a number: "))
sum = 0
temp = num
while temp > 0:
   d = temp % 10
   sum = sum + d ** 3
   temp = temp//10

if num == sum:
   print("Its Armstrong number")
else:
   print("Its not Armstrong number")