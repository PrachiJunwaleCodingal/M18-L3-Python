#Palindrome numbers
n= int(input("Enter number: "))
reverse = 0

temp = n
while temp>0:
    remen = temp%10
    reverse = remen + (reverse*10)
    temp = int(temp/10)

if reverse==n:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")