#ACP-Reverse number
num = int(input("Enter number:"))
rev = 0
while num != 0:
  c=num % 10
  rev=rev*10 +c
  num=num//10

print("Reversed order:",rev)
