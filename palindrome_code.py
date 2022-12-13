num=int(input('Please enter a number: '))

y=0

while(num>0):
    digit = num%10
    y = y+digit
    num = num//10

print("The total sum of digits is:",y)