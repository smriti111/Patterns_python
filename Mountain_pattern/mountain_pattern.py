
'''
n=10
row =5
    *
   * *
  *   *
 *     * *
*       *
'''


#row = 4
row=int(input("enter the no of rows "))
#n = 25
n=int(input("enter the no of stars "))
flag = 1
for i in range(row):
    flag = 1
    space_out = row-i-1
    print(' '*space_out,end='')
    print('*',end='')
    j = space_out+1
    while(j<n):
        space = 0
        if flag == 1:
            space = (2*row-1)-(2*(row-i))
            space = space if space>0 else 0
        elif flag == 2:
            space = (2*row-1)-(2*(i+1))
            space = space if space>0 else 0
        print(' '*space,end='')
        j+= space
        if j<n and space>0:
            print('*',end='')
            j+=1
        
        flag = 1 if flag==2 else 2
    print()
        
