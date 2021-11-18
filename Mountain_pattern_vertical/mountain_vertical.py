import math
row=int(input("Enter the number of rows "))
n=int(input("Enter the number of stars "))
half_n=2*row-2
if n>=1:
    print('*')
for j in range(1,n):
    factor=math.ceil(j/(half_n//2))
    if (j%half_n)>0 and (j%half_n)<=half_n/2: 
        print(' '*(j%half_n)+'*')
    else:
        space= half_n-(j%half_n) if half_n-(j%half_n)!=half_n else 0
        print(' '*space+'*')

        
