from vector import Vector

v = Vector()
v2 = Vector()
v2.push_back(50)
v2.push_back(3)
v.push_back(2)
v.push_back(4)
print(v.back())
print(v2.back())
print(v.front())
print(v2.front())
print(v.size_of_vector())
print(v2.size_of_vector())
v.copy_vector(v2)
v.print_vector()