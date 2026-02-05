'''


a = {1,2,3,4,5}
b = {4,5,6,7,8}


'''

A=set(map(int, input("Enter elements of Set A (Separated by space): ").split()))
B=set(map(int, input("Enter elements of Set B (Separated by space): ").split()))


Union = A.union(B)
Intersection = A.intersection(B)
Difference = A.difference(B)


'''
union_result = a | b

intersection_result = a.intersection(b)

defference_result = a.difference(b)'''

print("\nSet A : ",A)
print("Set B : ",B)
print("A union B is : ",Union)
print("A intesection B is : ",Intersection)
print("Difference of A and B is : ",Difference)