# Integer to string class change
a=112233
print(type(a))
print(a+5) # here performing arithmatic oprations bcause a is integer here
a=str(a) #at this stage class of a is changed to string
print(type(a)) #at this stage see class type
# print(a+5) # at this stage sum operation is not performing due to error change in data type
'''if syntax error at line 7 then futher program can not show output whatever you type, 
frist solve error or make it to statement '''
# String to int class change.
a="112233"
a=int(a) #changing class type string to int
print(a+5)
a=float(a+5)
print(a+5)

