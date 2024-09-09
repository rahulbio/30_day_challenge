array=[0, 1, 2, 1, 0, 2, 1, 0]


count_0=array.count(0)
count_1=array.count(1)
count_2=array.count(2)



element=0


for i in range(count_0):
    array[element]=0
    element+=1


for j in range(count_1):
    array[element]=1
    element+=1

for k in range(count_2):
    array[element]=2
    element+=1



print(array)