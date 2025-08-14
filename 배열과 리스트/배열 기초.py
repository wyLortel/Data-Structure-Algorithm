# 인덱스 값 조회 와 인덱스 값 업데이트 
arr = [22,36,45,44,21,24,82,11]

print(arr[3])

arr[5] = 16

print(arr)


#원하는 값의 인덱스 찾기 배열 한번씩 돌기

arr = [27,36,45,44,21,16,82,11]

for i in range(len(arr)):
    if arr[i] == 45:
        print(i)
        break


for val in arr:
    print(val)