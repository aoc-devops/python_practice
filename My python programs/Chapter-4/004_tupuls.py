# data in touple can not be modified once touple created
t=("harry", 5555, 50.20, "shobha", False, True)
print(type(t))
print(type(t[1]))
# print elements from touple
print(t[2])
print(t[2:])
# Cannot update the values of a tuple
# t[0] = 34 # throws an error