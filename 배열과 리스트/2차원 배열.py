arr = [[1,2,3,4],
       [5,6,7,8],
       [9,10,11,12]]


print(arr[1][2])

arr[1][2] = 99

for i in range(3):
    for j in range(4):
        if arr[i][j] == 10:
            print((i,j))


for val in arr[1]:
    print(val,end=" ")
    
    
print()

for i in range(3):
    print(arr[i][2] , end=" ")
    
print()
    
for row in arr:
    for val in row:
        print(val, end=" ")
    