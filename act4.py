#HCF- Highest Common Factor
num1 = float(input("Enter Num1 : "))
num2 = float(input("Enter Num2 : "))

while(num2 != 0):
    temp = num2
    num2 = num1 % num2
    num1 = temp

HCF = num1   
print("HCF is",HCF)

