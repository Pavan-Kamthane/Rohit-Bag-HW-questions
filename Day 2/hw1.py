# taking inputs

# as we need integer values mention in question so  we will use int() function to convert string to integer

a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))

def cube(num):
    # many method u just have to find
    # return num ** 3
    # or
    return num * num * num


# why a,b+1  is used here?
# because in range function 2ed parameter is exculded hence b+1

# we want sum of all numbers cube between a and b
# declear sum variable
sum = 0
for i in range(a,b+1):
    sum  =  sum + cube(i)
    
# print sum
print(sum)