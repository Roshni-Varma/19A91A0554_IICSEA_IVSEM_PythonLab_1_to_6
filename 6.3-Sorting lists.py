L1=[45,63,23,12,78]
L2=[12,90,72,-1]
combine L1 and L2 as a single list
and display elements in the sorted order
"""
l1=[]
l2=[]
n1=int(input("Enter number of elements in list 1:"))
for i in range(1,n1+1):
    b=int(input("Enter element:"))
    l1.append(b)
n2=int(input("Enter number of elements in list 2:"))
for i in range(1,n2+1):
    d=int(input("Enter element:"))
    l2.append(d)
new=l1+l2
new.sort()
print("Sorted list is:",new)

#output
Enter number of elements in list 1:4
Enter element:11
Enter element:14
Enter element:10
Enter element:13
Enter number of elements in list 2:3
Enter element:3
Enter element:2
Enter element:6
Sorted list is: [2, 3, 6, 10, 11, 13, 14]
