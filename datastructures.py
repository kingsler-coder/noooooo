# list datastructure
# list are mutable
# list are ordered
# list are indexed
fruits=['apple','banana','mango', 'orange', 'pineapple', 'pear']
fruits[0]="watermelon"
numbers= [1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers2= [67, 5, 56, 13, 80, 43, -7, -85]
numbers2.sort(reverse=True)
print(fruits)
numbers.append(11)
print(numbers)
print(f"I love eating {fruits[3]}")
print(numbers2)
# tuple datastructures
# tuples are immutable(unchanged)
# tuples are ordered
# tuples are indexed
cars=('audi', 'toyota','subaru','mercedes','honda')
print(cars)
nambari=(43,5,87,2,1,-3,-9,-100,-2345,-434,78)
# nambari.sort(reverse=True)
print(sorted(nambari))
print(nambari)
print(sorted(nambari))
# set datastructure
# set are unordered
# set are not indexed

computers={'dell','hp','thinkpad','lenovo','ibm','toshiba','mac'}
computers.add('google')
computers.remove('lenovo')

print(computers)
num1={1,2,3}
num2={4,6,7}
union_set=num1.union(num2)
print(union_set)
# Dictionaries data structure
student={'Name':'john','Age':5,'Gender':'Male','school':"university of Nairobi"}
print(student['Name'])
print(f"student Name:{student['Name']}")
print(f"student Age:{student['Age']}")
print(f"student Gender:{student['Gender']}")
print(f"student school:{student['school']}")