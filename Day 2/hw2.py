# to print:
'''
1 7 12 16 19 21
2 8 13 17 20
3 9 14 18 
4 10 15
5 11
6
'''
# take input
# n  = int(input("Enter a number: "))
# for now 
n = 6
# if you can see the diff between column is 6 ,5,4,3,2,


# outer loop for row
for i in range(1,n+1):
    num=i
    diff = n #6
    
    # inner loop for column
    for j in range((n+1)-i): 
        print(num,end=" ")
        num=num + diff
    
    diff=diff -1 #5,4,3,2,1

    print() # for new line




    
