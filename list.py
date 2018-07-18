mylist = [1,2,3, "saadas","a"]
print(len(mylist))
mylist[0]= "Trace"
#After reassignment
print(mylist)
mylist.append("Last")
print(mylist)
list2= ['s',2,'f']
mylist.extend(list2)
print(mylist)
print(mylist.pop())
mylist.reverse()
print(mylist)
mylist.sort()
print(mylist)

#ListCohension
matrix= [[1,2,3],[4,5,6,],[7,8,9]]
first_col = [row[0] for row in matrix]
print(first_col)