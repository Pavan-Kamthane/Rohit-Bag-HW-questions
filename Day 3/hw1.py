'''
input: 12345
output: 

    1               5
        2       4
            3
        2       4
    1               5
    
input : PAVAN

output:
    P               N
        A       A
            V
        A       A
    P               N
    
Note: length of input should be odd
'''

# expression

exp = input("Enter your expression: ")

if len(exp) % 2 == 0:
    print("Length is even not allowed")
else:
    # outer loop for rows
    for row in range(len(exp)):
        # inner loop for col
        for col  in range(len(exp)):
            if (row == col) or  (row + col == len(exp) - 1):
                print(exp[col], end=" ")
            else:
                print(" ",end=" ")
        
        print()


