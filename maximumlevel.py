def twospower(num ):
    
    for i in range(num):
        if  (2 ** i) == num:
            return 2 ** i
        elif (2 ** i) > num:
            return 2**(i - 1)

n = int(input("Enter the number: "))

concatedStr = ""

while n != 0:
    power = twospower(n)
    n = n - power # 16
    concatedStr = concatedStr + str(power)

print(concatedStr)
    