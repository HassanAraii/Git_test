my_list=1,2,3,4,4,3,2,2
lst={}

for i in my_list:
     lst[i]=lst.get(i,0)+1

print(lst)