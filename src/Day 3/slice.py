#list =[100,200,300,400,500,600,700,800,900]
#print(list[-1 : -3])
#we cannot give negative indexing in slicing
#print(list[1:4:3])
#1 is starting index 3 is skip value 4 is stop value
#print(list[-4 : -3 : 2])

#list are mutable
#append,insert,extend,remove,pop,clear,index,count,sort,reverse,copy
list1 = [5,10,15,20]

list1.reverse()
print(list1)
list1.append(25)
print(list1)
list1.insert(2,12)
print(list1)
list1.extend([30,35,40])
print(list1)
list1.remove(15)
print(list1)
list1.sort()
print(list1)

